'''我的首页'''
import streamlit as st
from PIL import Image
page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的推荐'''
    with open('霞光.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    tab1,tab2,tab3,tab4=st.tabs(['电影','游戏','书籍','习题'])
    with tab1:
        st.image('slogan.png')
        st.write('我的电影推荐')
        st.write('-----------------------------')
    with tab2:    
        st.write('我的游戏推荐')
        st.image('slogan.png')
        st.write('-----------------------------')
    with tab3:
        st.write('我的书籍推荐')
        st.image('slogan.png')
        st.write('-----------------------------')
    with tab4:
        st.write('我的习题集推荐')
        st.image('slogan.png')
        st.write('-----------------------------')

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 2, 0, 1))


def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
    
def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])

def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        with st.chat_message('🌞'):
            st.write(i[1],':',i[2])
    name =st.text_input('留言者姓名：')
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def page_5():
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if cb1==True and cb2 ==True and cb3==False and cb4 ==False:
            st.write('其实都不对，答案是“历史问题，不得已而为之”')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，下面就让我来讲讲吧！')
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '问卷调查':
    page_5()