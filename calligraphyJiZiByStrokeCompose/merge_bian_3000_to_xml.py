# coding: utf-8
import os
import shutil


chars = "一丁丂七万丈三上下丌不与丏丐丑专且丕世丘丙业丛东丝丞丢两严丽並丧丨丩个丫中丰串临丶丷丸义丹为主举丿乂乃久乇么之乌尹乍乎乏乐乒乓乔乖乘乙乚乛乜九乞也习书乩买乱乳乾亅了予争事二亍于亏云互亓五井亘亚些亟亠亡亢交亥亦产亨亩享京亭亮亲亵亶人亻亾亿什仁仂仃仄仅仆仇仉今介仌仍从仑仓仔仕他仗付仙仝仞仟仡代令以仨仪仫们仰仲仳仵件价任份仿企伉伊伍伎伏伐休众优伙会伛伞伟传伢伤伥伦伧伪伫佤伯估伲伴伶伸伺似伽佃但位低住佐佑体何佗佘余佚佛作佝佞佟你佣佥佧佩佬佯佰佳佴佶佻佼佾使侃侄侈侉例侍侏侑侔侗供依侠侣侥侦侧侨侩侪侬侮侯侵便促俄俅俊俎俏俐俑俗俘俚俜保俞俟信俣俦俨俩俪俭修俯俱俳俸俺俾倌倍倏倒倔倘候倚倜借倠倡倥倦倨倩倪倬倭倮债值倾偃假偈偌偎偏偕做停健偬偶偷偻偾偿傀傅傈傍傣傥傧储傩催傲傺傻像僕僖僚僦僧僬僭僮僳僵僻儆儇儋儒儡儿兀允元兄充兆先光克免兑兒兔兕兖党兜兟兢入全氽八公六兮兰共关兴兵其具典兹养兼兽冀冁冂内冈冉冊冋册再冏冒冓冕最冖冗冘写军农冠冡冢冤冥冫冬冯冰冱冲决况冶冷冻冼冽净凄准凇凉凋凌减凑凛凝几凡凤凫凭凯凰凳凵凶凸凹出击凼函凿刀⺈刁刂刃刅分切刈刊刍刎刑划刖列刘则刚创初删判刨利别刭刮到刳制刷券刹刺刻刽刿剀剁剂剃削剌前剐剑剔剖剜剞剡剥剧剪副剩割剽剿劁劂劈劐劓力劝办功加务劢劣劦动助努劫劬劭励劲劳劾势勃勇勉勋勐勒勖勘募勤勰勹勺勾勿匀包匆匈匊匋匍匏匐匕化北匙匚匛匝匠匡匣匦匪匮匸匹区医匽匾匿十卂千卅升午卉半华协卑卒卓单卖南博卜卞卟占卡卢卣卤卦卧卩卫卬卮卯印危即却卵卷卸卺卿厂厄厅历厉压厌厍厓厕厘厚厝原虒厢厣厩厥厦厨厮厶厷去厽县叁参又叉及友双反发叒叔叕取受变叙叚叛叟叠口古句另叨叩只叫召叭叮可台叱史右叵叶号司叹叻叼叽吁吂吃各吆合吉吊同名后吏吐向吒吓吕吖吗君吝吞吟吠吡吣否吧吨吩含听吭吮启吱吲吴吵吸吹吻吼吾呀呃呆呈告呋呐呒呓呔呕呖呗员呙呛呜呢呤呦周呱呲味呵呶呷呸呻呼命咀咂咄咅咆咋和咎咏咐咒咔咕咖咙咚咛咝咠咢咣咤咦咧咨咩咪咫咬咭咯咱咳咴咸咻咽咿哀品哂哄哆哇哈哉哌响哎哏哐哑哒哓哔哕哗哙哚哜哝哞哟哥哦哧哨哩哪哭哮哲哳哺哼哽哿唁唆唇唉唏唐唑唔唛唠唢唣唤唧唪唬售唯唰唱唳唷唼唾唿啁啃啄商啇啉啊啐啕啖啚啜啡啤啥啦啧啪啬啭啮啵啶啷啸啻啼啾喀喁喂喃善喇喈喉喊喋喏喑喔喘喙喜喝喟喧喱喳喵喷喹喻喽喾喿嗄嗅嗉嗌嗍嗑嗒嗓嗔嗖嗜嗝嗟嗡嗣嗤嗥嗦嗨嗪嗫嗬嗯嗲嗳嗵嗷嗽嗾嘀嘁嘈嘉嘌嘎嘏嘘嘛嘞嘣嘤嘧嘟嘬嘭嘱嘲嘴嘶嘹嘻嘿噌噍噎噔噗噘噙噜噢噤器噩噪噫噬噱噶噻噼嚅嚆嚎嚏嚓嚣嚯嚷嚼囊囔囗囚四囝回囟因囡团囤囫园困囱围囵囷囹固国图囿圂圃圄圆圈圉圊圜土圣圤在圩圪圬圭圮圯地圳圹场圻圼圾址坂均坊坌坍坎坏坐坑坒块坚坛坜坝坞坟坠坡坤坦坨坩坪坫坭坯坳坴坶坷坻坼垂垃垄垅垆型垌垒垓垔垛垠垡垢垣垤垦垧垩垫垭垮垲垴城垸埂埃埋埏埒埔埕埘埙埚埝域埠埤埭埯埴埸培基埽堀堂堆堇堋堍堑堕堙堞堠堡堤堪堰堵塄塌塍塑塔塘塞塥填塬塾墀墁境墅墉墓墙墚增墟墩墼壁壅壑壕壤士壬壮壯声壳壴壶壹夂夃处夅夆备夊夋夌复夏夔夕外夗夙多夜够夤夥大天太夫夬夭央夯失头夷夸夹夺夼奁奂奄奇奈奉奋奎奏契奔奕奖套奘奚奠奢奥女奴奶奸她好妁如妃妄妆妇妈妊妒妓妖妗妙妞妟妣妤妥妨妩妪妫妮妯妲妹妻妾姆姊始姐姑姒姓委姗妍姘姚姜姝姣姥姨姹姻姿威娃娅娆娇娈姬娉娌娑娓娘娜娟娠娣娥娩娱娲娴娶娼婀婆婉婊婕婚婢婧婪婴婵婶婷婺婿媒媚媛媪媲媳媵媷媸媾嫁嫂嫉嫌嫒嫔嫖嫘嫜嫠嫡嫣嫦嫩嫫嫱嬉嬖嬗嬴嬲嬷孀子孑孓孔孕字存孙孚孛孜孝孟孢季孤孥学孨孩孪孬孰孱孵孺孽宀宁它宄宅宇守安宋完宏宓宕宗官宙定宛宜宝实宠审客宣室宥宦宪宫宰害宴宵家宸容宽宾宿寂寄寅密寇富寐寒寓寝寞察寡寤寥寨寮寰寸对寺寻导寽寿封将尃射尉尊尌小少尔尕尖尗尘尚尜尝尞尢尤尥尧尬就尴尸尺尻尼尽尾尿局屁层居屈屉届屋屎屏屐屑展屙屚属屠屡屣履屦屮屯屰山屹屺屿岁岂岈岌岐岑岔岖岗岘岙岚岛岜岢岣岩岫岬岭岱岳岵岷岸岽岿峁峄岍峋峒峙峡峤峥峦峨峪峭峰峻崂崃崆崇崎崔崖崛崞崤崦崧崩崭崮崴崽崾嵇嵋嵌嵒嵘嵛嵝嵊嵩嵫嵬嵯嵴嶂嶙嶝嶷巅巍巛川州巢巤工左巧巨巩巫差巯己已巳巴巷巸巽巾巿币市布帅帆师希帏帐帑帔帕帖帘帙帚帛帜帝带帧席帮帱帷常帻帼帽幂幄幅幌幔幕幛幞幡幢干平年并幸幹乡幺幻幼幽广庀庄庆庇床庋序庐庑库应底庖店庙庚府庞废庠庥度座庭庳庵庶康庸庹庾廊廉廑廒廓廖廛廨廪廴延廷建廾廿开弁异弃弄弈弊弋式弒弓引弗弘弛弟张弥弦弧弩弪弭弯弱弹强弼彀彐彑归当录彖彗彘彝彡形彤彦彩彬彭彰影彳彷役彻彼往征徂径待徇很徉徊律後徐徒徕得徘徙徜御徨復循徭微徵德徼徽心忄必忆忉忌忍忏忐忑忒忖志忘忙忝忠忡忤忧忪快忭忮忱念忸忻忽忾忿怀态怂怃怄怅怆怊怍怎怏怒怔怕怖怙怛怜思怠怡急怦性怨怩怪怫怯怱怵总怼怿恁恂恃恋恍恐恒恕恙恚恝恢恣恤恧恨恩恪恫恬恭息恰恳恶恸恹恺恻恼恽恿悃悄悉悌悍悒悔悖悚悛悝悟悠患悤悦您悫悬悭悯悱悲悴悸悻悼情惆惊惋惑惕惘惚惜惝惟惠惢惦惧惨惩惫惬惭惮惯惰想惴惶惹惺愀愁愆愈愉愍愎意愕愚感愠愣愤愦慨愧愫愿慈慊慌慎慑慕慝慢慧慰慵慷憋憎憔憝憧憨憩憬憷憾懂懈懊懋懑懒懔懦懵懿戆戈戉戊戋戌戍戎戏成我戒戕或戗战戚戛戟戡戢戤戥截戬戮戴戳戶户戽戾房所扁扃扇扈扉手扌才扎扑扒打扔托扛扣扦执扩扪扫扬扭扮扯扰扳扶批扼找承技抄抉把抑抒抓投抖抗折抚抛抟抠抡抢护报抨披抬抱抵抹抻押抽抿拂拄担拆拇拈拉拊拌拍拎拐拑拒拓拔拖拗拘拙拚招拜拟拢拣拥拦拧拨择括拭拮拯拱拳拴拶拷拼拽拾拿持挂指挈按挎挑挖挚挛挝挞挟挠挡挢挣挤挥挨挪挫振挲挹挺挽捂捃捅捆捉捋捌捍捎捏捐捕捞损捡换捣捧捩捭据捱捶捷捺捻掀掂掇授掉掊掌掎掏掐排掖掘掠探掣接控推掩措掬掭掮掰掳掴掷掸掺掼掾揄揆揉揍揎描提插揖揞揠握揣揩揪揭揲援揶揸揽揿搀搁搂搅摒搋搌搏搐搓搔搛搜搞搠搡搦搪搬搭搴携搽搿摁摄摅摆摇摈摊摔摘摞摧摩摭摸摹摺撂撄撇撅撑撒撕撖撙撞撤撩撬播撮撰撵撷撸撺撼擀擂擅操擎擐擒擗擘擞擢擤擦攀攉攒攘攥攫攮支攴攵收攸改攻放政敃敄故效敉敌敏救敕敖教敛敝敞敢散敦敫敬数敲整敷文斋斌斐斑斓斗料斛斜斟斡斤斥斧斩斫断斯新方於施斿旁旃旄旅旆旉旋旌旎族旒旖旗无旡既日旦旧旨早旬旭旮旯旰旱时旷旺昀昂昃昆昊昌明昏易昔昕昙昝星映春昧昨昫昬昭是昱昴昵昶昷昼显晁晃晋晌晏晒晓晔晕晖晗晚晟晡晤晦晨普景晰晴晶晷智晾暂暑暄暇暌暖暗暝暧暨暮暴暹暾曙曛曜曝曦曩曰曲曳更曷曹曼曾替朁月有朊朋服朐朔朕朗望朝期朦木未末本札术朱朴朵机朽朿杀杂权杆杈杉杌李杏材村杓杖杜杞束杠条来杨杩极杪杭杯杰杲杳杵杷杼松板构枇枉枋析枕林枘枚果枝枞枢枣枥枧枨枪枫枭枯枰枳枵架枷枸枼柁柃柄柏某柑柒染柔柘柙柚柜柝柞柠柢查柩柬柯柰柱柳柴柽柿栀栅标栈栉栊栋栌栎栏树栓栖栗栝校栩株栲栳样核根格栽栾桀桁桂桃桄桅框案桉桊桌桎桐桑桓桔桕桠桡桢档桤桥桦桧桨桩桫桴桶桷桼梁梃梅梆梏梓梗梢梦梧梨梭梯械梳梵检棂棉棋棍棒棕棘棚棠棣棥森棰棱棵棹棺棼椁椅椋植椎椐椒椟椠椤椭椰椴椹椽椿楂楔楗楙楚楝楞楠楣楦楫楮楱楷楸楹楼榀概榄榆榇榈榉榔榘榍榕榛榜榧榨榫榭榱榴榷榻槁槊槌槎槐槔槛槟槠槭槲槽槿樊樗樘樟模樨横樯樱橥樵樽樾橄橇橐橘橙橛橡橱橹橼檀檄檎檐檑檗檠檩檫檬欠次欢欤欣欧欮欲欶欷欹欺款歃歆歇歉歌歙止正此步武歧歨歪歹歺死歼殁殂殃殄殆殇殉殊残殍殒殓殖殚殛殡殪殳殴段殷殸殹殿毁毂毅毋毌母每毒毓比毕毖毗毙毛毡毪毫毯毳毵毹毽氅氆氇氍氏氐民氓气氕氖氘氙氚氛氟氡氢氤氦氧氨氩氪氮氯氰氲水氵氺永氾氿汀汁求汆汇汉汊汐汒汔汕汗汛汜汝汞江池污汤汨汩汪汰汲汴汶汹汽汾沁沂沃沅沆沈沉沌沏沐沓沔沙沛沟没沣沤沥沦沧沩沪沫沭沮沱沲河沸油治沼沽沾沿泄泅泉泊泌泐泓泔法泖泗泙泛泞泠泡波泣泥注泪泫泮泯泰泱泳泶泷泸泺泻泼泽泾洁洄洇洋洌洎洒洗洙洚洛洞津洧洪洫洮洰洱洲洳洵洹活洼洽派流浃浅浆浇浈浊测浍济浏浑浒浓浔浙浚浜浞浠浣浦浩浪浮浯浴海浸浼涂涅消涉涌涎涑涓涔涕涛涝涞涟涠涡涣涤润涧涨涩涪涫涮涯液涵涸涿淀淄淅淆淇淋淌淑淖淘淙淝淞淠淡淤淦淫淬淮深淳混淹添淼清渊渌渍渎渐渑渔渖渗渚渝渠渡渣渤渥温渫渭港渲渴游渺湃湄湍湎湓湔湖湘湛湟湫湮湾湿溃溅溆溉滋滞溏源溘溜溟溢溥溧溪溯溱溲溴溶溷溺溻溽滁滂滇"

path = "/Users/liupeng/Documents/Data/Calligraphy_database/边倩楠/Chars"
save_path = "/Users/liupeng/Documents/Data/Calligraphy_database/边倩楠/chars_finished"

def merge_bian_3000_xml():
    count = 0

    for ch in chars:
        p = os.path.join(path, ch, "basic radicals")

        folders = [f for f in os.listdir(p) if ".png" not in f and "." not in f]
        imgs = []
        pngs = [f for f in os.listdir(p) if ".png" in f]

        for fl in folders:
            for pn in pngs:
                if fl == pn.replace(".png", ""):
                    imgs.append(pn)

                    print(ch)

                    if not os.path.exists(os.path.join(save_path, ch)):
                        shutil.copytree(os.path.join(path, ch), os.path.join(save_path, ch))

        if len(imgs) == len(folders) and len(imgs) > 0:
            print(ch)
            count += 1

        # remove other images
        for pn in pngs:
            if pn not in imgs:
                # remove this image
                if os.path.exists(os.path.join(save_path, ch, "basic radicals", pn)):
                    os.remove(os.path.join(save_path, ch, "basic radicals", pn))


if __name__ == '__main__':
    merge_bian_3000_xml()