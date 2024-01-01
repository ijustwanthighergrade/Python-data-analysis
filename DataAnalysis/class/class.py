data_dict = {}
listb=["生理性別", "最高學歷", "您的年齡", "目前月薪資水平(台幣)", "您是否已婚？",
            '您目前是否有結婚意願(不論單身與否)\n已婚者可以是否後悔結婚來考量', '您認同買房是影響多數人結婚的重要因素嗎？', '請問買房影響您結婚意願的程度為？', 
             '您對結婚一定得買房的認同度為何？', '請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？', '您認同買房會影響到個人生活水平的程度為？', 
             '您認為政府在買房上已擁有完善配套措施的程度為？', '可能使擁有結婚意願的因素：想要與心愛的人共組家庭', '可能使擁有結婚意願的因素：想要小孩', 
             '可能使擁有結婚意願的因素：想要讓伴侶關係被法律所認同', '可能使擁有結婚意願的因素：傳統上結婚是人生的必經之路', 
             '可能使擁有結婚意願的因素：想要伴侶一同承擔責任', '可能影響您結婚意願的經濟因素：不想因為結婚犧牲現有生活水平', 
             '可能影響您結婚意願的經濟因素：無法負擔高額房價', '可能影響您結婚意願的經濟因素：無法負擔結婚開銷', 
             '可能影響您結婚意願的經濟因素：想要先穩定事業再組建家庭', '可能影響您結婚意願的經濟因素：無法負擔子女教養費用', 
             '可能影響您結婚意願的非經濟因素：只需要情感需求，不想綁定法律義務', '可能影響您結婚意願的非經濟因素：害怕要與對方家庭磨合', 
             '可能影響您結婚意願的非經濟因素：不知是否對方值得信任', '可能影響您結婚意願的非經濟因素：不想養小孩', 
             '可能影響您結婚意願的非經濟因素：婚後會失去自由', '可能影響您結婚意願的非經濟因素：沒有對象', '可能影響您結婚意願的非經濟因素：害怕婚姻失敗']

# Categorize items with '的' as the main key
for item in listb:
    if '：' in item:
        main_key, sub_key = item.split('：', 1)
        main_key = main_key.strip()
        sub_key = sub_key.strip()
        if main_key not in data_dict:
            data_dict[main_key] = {}
        data_dict[main_key][sub_key] = None

    # Categorize items with '房' as the main key
    for item in listb:
        if '房' in item:
            main_key = '買房觀念'
            sub_key = item.strip()
            if main_key not in data_dict:
                data_dict[main_key] = {}
            data_dict[main_key][sub_key] = None

    # Categorize remaining items
    main_key = '一般資訊'
    for item in listb:
        if '的' not in item and '房' not in item:
            sub_key = item.strip()
            if main_key not in data_dict:
                data_dict[main_key] = {}
            data_dict[main_key][sub_key] = None

print(data_dict)