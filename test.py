from bbscode import converter

with open("test.md",'r',encoding='utf-8') as f:
    md_str = f.read()

bbscode = converter.md_to_bbscode(md_str)

print(bbscode)