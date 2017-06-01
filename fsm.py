from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

#==========first===========================
    def Going_init(self, update):
        text = update.message.text
        return text.lower() == '0'

    def Going_Beach(self, update):
        text = update.message.text
        return text.lower() == '1'

    def Going_Forest(self, update):
        text = update.message.text
        return text.lower() == '2'

    def Going_Town(self, update):
        text = update.message.text
        return text.lower() == '3'

    def Going_Mountain(self, update):
        text = update.message.text
        return text.lower() == '4'

    def Going_Underground(self, update):
        text = update.message.text
        return text.lower() == '5'
#==========second==========================
#====beach=========
    def Going_Sinkship(self, update):
        text = update.message.text
        return text.lower() == '1'
    def Going_Undersea(self, update):
        text = update.message.text
        return text.lower() == '2'
#====forest========
    def Going_Lake(self, update):
        text = update.message.text
        return text.lower() == '1'
    def Going_Plain(self, update):
        text = update.message.text
        return text.lower() == '2'
#====town==========
    def Going_Market(self, update):
        text = update.message.text
        return text.lower() == '1'
    def Going_Trainstation(self, update):
        text = update.message.text
        return text.lower() == '2'
    def Going_Tower(self, update):
        text = update.message.text
        return text.lower() == '3'
#====mountain======
    def Going_Spring(self, update):
        text = update.message.text
        return text.lower() == '1'
    def Going_Top(self, update):
        text = update.message.text
        return text.lower() == '2'
#====underground===
    def Going_Tomb(self, update):
        text = update.message.text
        return text.lower() == '1'
    def Going_Palace(self, update):
        text = update.message.text
        return text.lower() == '2'
#==========third===========================
#====beach=========
    def Sinkship_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Sinkship_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
    def Undersea_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Undersea_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
#====forest========
    def Lake_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Lake_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
    def Plain_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Plain_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
#====town==========
    def Market_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Market_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
    def Trainstation_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Trainstation_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
    def Tower_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Tower_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
#====mountain======
    def Spring_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Spring_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
    def Top_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Top_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
#====underground===
    def Tomb_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Tomb_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
    def Palace_Yes(self, update):
        text = update.message.text
        return text.lower() == 'y'
    def Palace_No(self, update):
        text = update.message.text
        return text.lower() == 'n'
#==========================================







#==========first===========================
    def on_enter_initial(self, update):
        update.message.reply_text("新的冒險開始了！你從家裡出發,有五條路可以走,請輸入1-5選擇一條路走吧")
        self.go_back(update)

    def on_enter_Beach(self, update):
        update.message.reply_text("你來到了海邊潛入了海中,選擇1前往沉船,選擇2前往深海")

    def on_exit_Beach(self, update):
        print('Leaving Beach')

    def on_enter_Forest(self, update):
        update.message.reply_text("你走進了一篇森林,選擇1前往湖畔,選擇2前往平原")

    def on_exit_Forest(self, update):
        print('Leaving Forest')

    def on_enter_Town(self, update):
        update.message.reply_text("你走進了一座城市,選擇1前往市場,選擇2前往車站,選擇3前往高塔")

    def on_exit_Town(self, update):
        print('Leaving Town')

    def on_enter_Mountain(self, update):
        update.message.reply_text("你爬上了一座山,選擇1前往溫泉處,選擇2前往山頂")

    def on_exit_Mountain(self, update):
        print('Leaving Mountain')

    def on_enter_UnderGround(self, update):
        update.message.reply_text("你走進了一處地下隧道,選擇1前往古墓,選擇2前往古城")

    def on_exit_Underground(self, update):
        print('Leaving Underground')
#==========second==========================
#====beach==============
    def on_enter_Sinkship(self, update):
        update.message.reply_text("沉船中似乎有個神祕船艙,輸入y選擇進入,輸入n選擇不進入")

    def on_exit_Sinkship(self, update):
        print('Leaving Sinkship')

    def on_enter_Undersea(self, update):
        update.message.reply_text("你在海底看到了一條金閃閃的魚,輸入y選擇跟隨,輸入n選擇不跟隨")

    def on_exit_Undersea(self, update):
        print('Leaving Undersea')
#====forest=============
    def on_enter_Lake(self, update):
        update.message.reply_text("湖中似乎有東西閃爍著,輸入y選擇跳入湖中尋找,輸入n選擇不跳湖")

    def on_exit_Lake(self, update):
        print('Leaving Lake')

    def on_enter_Plain(self, update):
        update.message.reply_text("廣大的平原中有棵發光的樹,輸入y選擇前往,輸入n選擇回頭")

    def on_exit_Plain(self, update):
        print('Leaving Plain')
#====town===============
    def on_enter_Market(self, update):
        update.message.reply_text("來到了市場恰巧碰上盜賊搶劫,輸入y選擇追擊,輸入n選擇放棄")

    def on_exit_Market(self, update):
        print('Leaving Market')

    def on_enter_Trainstation(self, update):
        update.message.reply_text("進入車站時恰巧有炸彈客站在車站中央威脅,輸入y選擇撲向他,輸入n選擇不理會")

    def on_exit_Trainstation(self, update):
        print('Leaving Trainstation')

    def on_enter_Tower(self, update):
        update.message.reply_text("登上塔頂時有怪獸襲擊了城市,輸入y選擇與牠戰鬥,輸入n選擇逃跑")

    def on_exit_Tower(self, update):
        print('Leaving Tower')
#====mountain===========
    def on_enter_Spring(self, update):
        update.message.reply_text("來到溫泉卻發現溫泉正在枯萎,輸入y選擇調查原因,輸入n選擇不理會")

    def on_exit_Spring(self, update):
        print('Leaving Spring')

    def on_enter_Top(self, update):
        update.message.reply_text("你終於爬上山頂卻碰上山崩,輸入y選擇阻擋,輸入n選擇逃離")

    def on_exit_Top(self, update):
        print('Leaving Top')
#====underground========
    def on_enter_Tomb(self, update):
        update.message.reply_text("你發現了一座埋著許多財寶的古墓,輸入y選擇拿取財寶,輸入n選擇無視")

    def on_exit_Tomb(self, update):
        print('Leaving Tomb')

    def on_enter_Palace(self, update):
        update.message.reply_text("你發現了一座埋於地底的古代宮殿,輸入y選擇膜拜帝王像,輸入n選擇偷取帝王像")

    def on_exit_Palace(self, update):
        print('Leaving Palace')
#==========third===========================
#====beach==============
    def on_enter_SinkshipY(self, update):
        update.message.reply_text("你被鯊魚咬了,死在沉船中")
        self.go_back(update)

    def on_exit_SinkshipY(self, update):
        print('Leaving SinkshipY, back to title.')

    def on_enter_SinkshipN(self, update):
        update.message.reply_text("你轉往另一個房間,發現了一堆古金幣,發了一筆大財")
        self.go_back(update)

    def on_exit_SinkshipN(self, update):
        print('Leaving SinkshipN, back to title.')

    def on_enter_UnderseaY(self, update):
        update.message.reply_text("你抓到了一隻稀有的魚,這隻魚為你帶來了財富和名聲")
        self.go_back(update)

    def on_exit_UnderseaY(self, update):
        print('Leaving UnderseaY, back to title.')

    def on_enter_UnderseaN(self, update):
        update.message.reply_text("在你猶豫時,你被海流帶到陌生的地方,最後絕氣而死")
        self.go_back(update)

    def on_exit_UnderseaN(self, update):
        print('Leaving UnderseaN, back to title.')
#====forest=============
    def on_enter_LakeY(self, update):
        update.message.reply_text("你跳進湖裡卻什麼都沒找到,淹死在湖中")
        self.go_back(update)

    def on_exit_LakeY(self, update):
        print('Leaving LakeY, back to title.')

    def on_enter_LakeN(self, update):
        update.message.reply_text("湖中浮出湖中女神,她送你一支金iphone跟一支銀iphone")
        self.go_back(update)

    def on_exit_LakeN(self, update):
        print('Leaving LakeN, back to title.')

    def on_enter_PlainY(self, update):
        update.message.reply_text("你走到那棵樹下,撿到了稀有的果子,發了一筆大財")
        self.go_back(update)

    def on_exit_PlainY(self, update):
        print('Leaving PlainY, back to title.')

    def on_enter_PlainN(self, update):
        update.message.reply_text("你往回走,卻遇上一隻獅子,被牠咬死")
        self.go_back(update)

    def on_exit_PlainN(self, update):
        print('Leaving PlainN, back to title.')
#====town===============
    def on_enter_MarketY(self, update):
        update.message.reply_text("你追到了那個盜賊,盜賊反刺你一刀,你倒在血泊中死去")
        self.go_back(update)

    def on_exit_MarketY(self, update):
        print('Leaving MarketY, back to title.')

    def on_enter_MarketN(self, update):
        update.message.reply_text("你不逞英雄,迅速叫了警察,警察成功抓到盜賊,你被警察表揚了一番")
        self.go_back(update)

    def on_exit_MarketN(self, update):
        print('Leaving MarketN, back to title.')

    def on_enter_TrainstationY(self, update):
        update.message.reply_text("你英勇且俐落的解決炸彈客,拯救了全車站的人")
        self.go_back(update)

    def on_exit_TrainstationY(self, update):
        print('Leaving TrainstationY, back to title.')

    def on_enter_TrainstationN(self, update):
        update.message.reply_text("你的猶豫讓時間過去,炸彈爆炸,你跟其他人死於爆炸中")
        self.go_back(update)

    def on_exit_TrainstationN(self, update):
        print('Leaving TrainstationN, back to title.')

    def on_enter_TowerY(self, update):
        update.message.reply_text("你發現了怪獸的死穴,跳出塔將牠一擊斃命,拯救了全城市的人")
        self.go_back(update)

    def on_exit_TowerY(self, update):
        print('Leaving TowerY, back to title.')

    def on_enter_TowerN(self, update):
        update.message.reply_text("怪獸一掌揮倒了塔,你跟著塔一起墜至地面死去")
        self.go_back(update)

    def on_exit_TowerN(self, update):
        print('Leaving TowerN, back to title.')
#====mountain===========
    def on_enter_SpringY(self, update):
        update.message.reply_text("你觀察溫泉,發現了問題所在,溫泉再度泉湧而出")
        self.go_back(update)

    def on_exit_SpringY(self, update):
        print('Leaving SpringY, back to title.')

    def on_enter_SpringN(self, update):
        update.message.reply_text("你無視溫泉,溫泉枯竭,而你被當作破壞溫泉的嫌疑犯,移送法辦")
        self.go_back(update)

    def on_exit_SpringN(self, update):
        print('Leaving SpringN, back to title.')

    def on_enter_TopY(self, update):
        update.message.reply_text("你擋不住山崩,滾落至山腳摔死")
        self.go_back(update)

    def on_exit_TopY(self, update):
        print('Leaving TopY, back to title.')

    def on_enter_TopN(self, update):
        update.message.reply_text("你不逞強,閃開了山崩,活了下來,成功攻頂")
        self.go_back(update)

    def on_exit_TopN(self, update):
        print('Leaving TopN, back to title.')
#====underground========
    def on_enter_TombY(self, update):
        update.message.reply_text("你侵犯了古墓的魂魄,你被詛咒,終生永遠出不去這個古墓")
        self.go_back(update)

    def on_exit_TombY(self, update):
        print('Leaving TombY, back to title.')

    def on_enter_TombN(self, update):
        update.message.reply_text("你的謹慎讓你免於被詛咒,並讓你發現另一處值得考古的墓穴,你成了世界名人")
        self.go_back(update)

    def on_exit_TombN(self, update):
        print('Leaving TombN, back to title.')

    def on_enter_PalaceY(self, update):
        update.message.reply_text("古代帝王的英靈敬仰你的勇氣,讓你帶得許多財寶與古物回家")
        self.go_back(update)

    def on_exit_PalaceY(self, update):
        print('Leaving PalaceY, back to title.')

    def on_enter_PalaceN(self, update):
        update.message.reply_text("古代帝王因為你的無禮而發怒,你終生被困在古城中,永不見天日")
        self.go_back(update)

    def on_exit_PalaceN(self, update):
        print('Leaving PalaceN, back to title.')
