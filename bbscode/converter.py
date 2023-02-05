import re
def replace_quote(matched):
    quote = matched.group(1)
    quote = re.sub(r"> (.*?)","",quote)
    quote = "[quote]\n{}\n[/quote]".format(quote)
    return quote
def replace_list(matched):
    l = matched.group(1)
    l = re.sub(r"[-*] ","[*]",l)
    l = "[list]\n{}\n[/list]".format(l)
    return l
def replace_italic(matched):
    # 到了第53个中文字符的时候NGA论坛就会报错：一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十一二三/* bbscode i too long */
    # 所以需要每50个字符就分一个[i]标签
    italic = matched.group(1)
    step = 40
    italics = [italic[i:i+step] for i in range(0,len(italic),step)]
    italic = ''
    for item in italics:
        italic +="[i]{}[/i]".format(item)

    return italic
def replace_collapse(matched):
    '''
    <details>
        <summary>点击查看详细内容</summary>
    </details>
    '''
    collapse = matched.group(1)
    summary = re.findall(r"<summary>(.*?)</summary>",collapse,flags=re.DOTALL)
    collapse = re.sub(r"<summary>(.*?)</summary>","",collapse,flags=re.DOTALL)
    if summary:# 有标题
        summary = re.sub(r"\n",r" ",summary[0])
        collapse = "[collapse={}]{}[/collapse]".format(summary,collapse)
    else:
        collapse = "[collapse]{}[/collapse]".format(collapse)

    return collapse


def md_to_bbscode(md_str:str):
    '''
    将markdown字符串转换为bbscode字符串
    '''
    bbscode = md_str
    # 链接
    bbscode = re.sub(r"[^!]\[(.*?)\]\((.*?)\)",r"[url=\2]\1[/url]",bbscode)
    # 图片
    bbscode = re.sub(r"\!\[(.*?)\]\((.*?)\)",r"[img]\2[/img]",bbscode)
    # 标题，注意设置flag为MULTILINE以改变^的语义
    bbscode = re.sub(r"^(#+)\s?(.*)",r"[align=center][size=150%][b]\2[/b][/size][/align]",bbscode,flags=re.MULTILINE)
    # 加粗
    bbscode = re.sub(r"\*\*(.*?)\*\*",r"[b]\1[/b]",bbscode,flags=re.DOTALL)
    # 斜体
    bbscode = re.sub(r"\*(.*?)\*",replace_italic,bbscode,flags=re.DOTALL)
    # 下划线
    bbscode = re.sub(r"<u>(.*?)</u>",r"[u]\1[/u]",bbscode,flags=re.DOTALL)
    # 删除线
    bbscode = re.sub(r"~~(.*?)~~",r"[del]\1[/del]",bbscode,flags=re.DOTALL)
    # 引用块
    bbscode = re.sub(r"((> (.*)\n?)+)",replace_quote,bbscode,flags=re.DOTALL)
    # 列表
    bbscode = re.sub(r"(([-|*] (.*)\n?)+)",replace_list,bbscode,flags=re.DOTALL)
    # 折叠
    bbscode = re.sub(r"<details>(.*?)</details>",replace_collapse,bbscode,flags=re.DOTALL)

    return bbscode