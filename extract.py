
def extract_js_fragment(js: str, label: str, flags: str) -> str:
    """
    从源 js 代码中提取 label 标记的代码
    :param js: 源 js 代码
    :param label: 标签
    :param flags: 代码块开始和结束的标志，比如 '()','[]','{}'
    :return: label 标记的代码片段
    """
    start_index = js.find(label+':') + len(label) + 1
    # 查找第一个 flag
    i = start_index
    while i < len(js):
        if js[i] == flags[0]:
            break
        else:
            i += 1
    # 查找第一个 flags[0] 对应的 flags[1]
    i += 1
    count = 1
    while i < len(js):
        if js[i] == flags[1]:
            count -= 1
            if count == 0:
                break
        elif js[i] == flags[0]:
            count += 1
        i += 1

    return js[start_index:i + 1] + ';'


def extract_name_table_js(js: str) -> str:
    """
    提取源 js 中的名称列表定义语句
    :param js: js源代码
    :return: 名称表定义语句
    """
    return extract_js_fragment(js=js, label='name_table', flags='[]')


def extract_shift_js(js: str) -> str:
    """
    提取源 js 代码中的名称列表倒转方法的代码
    :param js: 源 js 代码
    :return: 倒转名称表的方法
    """
    return extract_js_fragment(js=js, label='shift_function', flags='()')


def extract_name_query_js(js: str) -> str:
    """
    提取源 js 代码中的查询名称用的方法代码
    :param js: 源 js 代码
    :return: 源 js 中查询名称的方法代码
    """
    return extract_js_fragment(js=js, label='name_query', flags='{}')
