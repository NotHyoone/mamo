from __future__ import annotations

import sys
import tempfile
from pathlib import Path

import markdown
from pyhwpx import Hwp


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang=\"ko\">
<head>
  <meta charset=\"utf-8\" />
  <title>{title}</title>
  <style>
    body {{
      font-family: "Malgun Gothic", "맑은 고딕", sans-serif;
      line-height: 1.6;
      margin: 36px;
      font-size: 11pt;
    }}
    h1, h2, h3 {{
      margin-top: 1.2em;
      margin-bottom: 0.5em;
    }}
    h1 {{ font-size: 20pt; }}
    h2 {{ font-size: 16pt; }}
    h3 {{ font-size: 13pt; }}
    p, li {{ margin: 0.35em 0; }}
    code {{
      font-family: Consolas, "Courier New", monospace;
      background: #f5f5f5;
      padding: 0.1em 0.25em;
    }}
    pre {{
      background: #f5f5f5;
      border: 1px solid #d9d9d9;
      padding: 12px;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-word;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 18px;
      font-size: 10.5pt;
    }}
    th, td {{
      border: 1px solid #666;
      padding: 6px 8px;
      vertical-align: top;
    }}
    th {{
      background: #efefef;
      text-align: center;
    }}
    blockquote {{
      margin: 12px 0;
      padding: 8px 12px;
      border-left: 4px solid #999;
      background: #fafafa;
    }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def build_html(markdown_text: str, title: str) -> str:
    body = markdown.markdown(
        markdown_text,
        extensions=["tables", "fenced_code", "md_in_html", "sane_lists"],
        output_format="html5",
    )
    return HTML_TEMPLATE.format(title=title, body=body)


def convert_markdown_to_hwpx(source_path: Path, output_path: Path) -> None:
    markdown_text = source_path.read_text(encoding="utf-8")
    html = build_html(markdown_text, source_path.stem)

    with tempfile.TemporaryDirectory() as temp_dir:
        html_path = Path(temp_dir) / f"{source_path.stem}.html"
        html_path.write_text(html, encoding="utf-8")

        hwp = Hwp(new=True, visible=False, register_module=True)
        try:
            opened = hwp.open(str(html_path), format="HTML")
            if not opened:
                raise RuntimeError("HTML 파일을 한글에서 열지 못했습니다.")

            saved = hwp.save_as(str(output_path), format="HWPX")
            if not saved:
                raise RuntimeError("HWPX 파일 저장에 실패했습니다.")
        finally:
            try:
                hwp.clear()
            except Exception:
                pass
            try:
                hwp.FileClose()
            except Exception:
                pass
            try:
                hwp.quit()
            except Exception:
                pass


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("usage: convert_md_to_hwpx.py <source.md> [output.hwpx]")
        return 1

    source_path = Path(sys.argv[1]).resolve()
    if not source_path.exists():
        print(f"source file not found: {source_path}")
        return 1

    if len(sys.argv) == 3:
        output_path = Path(sys.argv[2]).resolve()
    else:
        output_path = source_path.with_suffix(".hwpx")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    convert_markdown_to_hwpx(source_path, output_path)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())