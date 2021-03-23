def date_sorter():


    months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    months_full = {'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09','October':'10','Nov':'11','Dec':'12'}
    layout1 = r'(\d{1,2})[/](\d{1,2})[/](\d{2,4})' # 4/10/96
    layout2 = r'(\d{1,2})[-](\d{1,2})[-](\d{2,4})' # 3-7-99

    layout3 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[.]?[- ](\d{1,2})[,]?[- ](\d{4})'

    layout4 = r'(\d{1,2}) ((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[.,]? (\d{4})' # Jun, 1982

    layout21 = r'(\d{1,2}) ((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[,]? (\d{4})'

    layout8 = r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[a-z]*[,]? (\d{4})'

    layout10 = r'(\d{1,2})[/](\d{4})'

    layout11 = r'\d{4}'

    nice_list = []
    for line in df :

        #layout1
        if len(re.findall(layout1, line)) != 0 :
            focus_date = list(re.findall(layout1, line)[0])
            if len(focus_date[2]) == 2 :
                focus_date[2] = '19' + focus_date[2]
            if len(focus_date[0]) == 1 :
                focus_date[0] = '0' + focus_date[0]
            if len(focus_date[1]) == 1 :
                focus_date[1] = '0' + focus_date[1]
            #print(focus_date)
            interim = focus_date[2] + focus_date[0] + focus_date[1]
            nice_list.append(interim)

        #layout2
        elif len(re.findall(layout2, line)) != 0 :
            focus_date = list(re.findall(layout2, line)[0])
            #print(focus_date)
            if len(focus_date[2]) == 2 :
                focus_date[2] = '19' + focus_date[2]
            if len(focus_date[0]) == 1 :
                focus_date[0] = '0' + focus_date[0]
            if len(focus_date[1]) == 1 :
                focus_date[1] = '0' + focus_date[1]
            #print(focus_date)
            interim = focus_date[2] + focus_date[0] + focus_date[1]
            nice_list.append(interim)

        #layout3

        elif len(re.findall(layout3, line)) != 0 :

            focus_date = list(re.findall(layout3, line)[0])
            #print(focus_date)
            if len(focus_date[2]) == 2 :
                focus_date[2] = '19' + focus_date[2]
            if len(focus_date[1]) == 1 :
                focus_date[1] = '0' + focus_date[1]
            focus_date[0] = months[focus_date[0]]
            interim = focus_date[2] + focus_date[0] + focus_date[1]
            nice_list.append(interim)
            #print(interim)

        #layout21
        elif len(re.findall(layout21, line)) != 0 :
            #print(line)
            focus_date = list(re.findall(layout21, line)[0])
            #print(focus_date)
            if len(focus_date[0]) == 1 :
                focus_date[0] = '0' + focus_date[0]
            focus_date[1] = months[focus_date[1]]
            interim = focus_date[2] + focus_date[1] + focus_date[0]
            #print(interim)
            nice_list.append(interim)

        #layout8
        elif len(re.findall(layout8, line)) != 0 :
            #print(line)
            focus_date = list(re.findall(layout8, line)[0])
            #print(focus_date)
            focus_date[0] = months[focus_date[0]]
            interim = focus_date[1] + focus_date[0] + '01'
            #print(interim)
            nice_list.append(interim)

        #layout10
        elif len(re.findall(layout10, line)) != 0 :
            focus_date = list(re.findall(layout10, line)[0])
            #print(focus_date)
            if len(focus_date[0]) == 1 :
                focus_date[0] = '0' + focus_date[0]
            interim = focus_date[1] + focus_date[0] + '01'
            #print(interim)
            nice_list.append(interim)

        #layout11
        elif len(re.findall(layout11, line)) != 0 :
            focus_date = list(re.findall(layout11, line)[0])
            #print(focus_date)
            interim = focus_date[0]+focus_date[1]+focus_date[2]+focus_date[3]+'01'+'01'
            #print(interim)
            nice_list.append(interim)


    df_d = pd.Series(nice_list)
    df_d = pd.to_datetime(df_d)

    df_d.sort_values(inplace=True)
    answ = pd.Series(df_d.index)

    return answ
