from __future__ import unicode_literals

from django.db import models


# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名', max_length=32, db_index=True)  # db_index=True 索引
    email = models.EmailField(verbose_name='邮箱', max_length=32)
    mobile_phone = models.CharField(verbose_name='手机号', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    def __str__(self):
        return 'user:{}'.format(self.username)


class LunTan(models.Model):
    # user = models.OneToOneField(UserInfo, on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(verbose_name="yh", max_length=30, default="admin", null=True, blank=True)

    title = models.CharField(verbose_name="标题", max_length=30, default="")
    leixing_choices = (  # 新建选择字段
        (1, '文章'),
        (2, '课程'),
    )
    leixing = models.SmallIntegerField(verbose_name="类型", choices=leixing_choices, default=1)
    jianjie = models.TextField(verbose_name="简介", max_length=1550, default="")
    # 本质上数据库也是CharField，自动保存数据。

    content = models.TextField(verbose_name="帖子内容", max_length=1000, default="")
    Count = models.IntegerField(verbose_name="浏览次数", default=0)
    img = models.FileField(verbose_name="图片", max_length=128, upload_to='luntan/', default="")


class History(models.Model):
    # user = models.OneToOneField(UserInfo, on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(verbose_name="yh", max_length=30, default="", null=True, blank=True)
    content = models.TextField(verbose_name="内容", max_length=300)

class Person1(models.Model):
    user = models.CharField(verbose_name="yh", max_length=30,  default="这个人什么都没有写")
    birth = models.CharField(verbose_name="生日", max_length=100, blank=True, null=True, default="这个人什么都没有写")

    school = models.CharField(verbose_name="学校", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    company = models.CharField(verbose_name="公司", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    profession = models.CharField(verbose_name="职业或专业", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    address = models.CharField(verbose_name="住址", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    about = models.TextField(verbose_name="其他", blank=True, null=True, default="这个人什么都没有写")


class Person(models.Model):
    user = models.CharField(verbose_name="yh", max_length=30,  default="这个人什么都没有写")
    birth = models.CharField(verbose_name="生日", max_length=100, blank=True, null=True, default="这个人什么都没有写")

    school = models.CharField(verbose_name="学校", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    company = models.CharField(verbose_name="公司", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    profession = models.CharField(verbose_name="职业或专业", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    address = models.CharField(verbose_name="住址", max_length=100, blank=True, null=True, default="这个人什么都没有写")
    about = models.TextField(verbose_name="其他", blank=True, null=True, default="这个人什么都没有写")

    # def __str__(self):
    #     return 'user:{}'.format(self.user.username)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.cleaned_data = None

    def is_valid(self):
        pass


class Book(models.Model):
    book_name = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class surveys(models.Model):
    # 1.学校 姓名 学院 老师 学号 班级
    school = models.CharField('学校', max_length=24, default=None, blank=True)
    user = models.CharField('姓名', max_length=24, default=None, blank=True)
    college = models.CharField('学院', max_length=12, default=None, blank=True)
    teacher = models.CharField('老师', max_length=128, default=None, blank=True)
    edu_number = models.CharField('学号', max_length=24, default=None, blank=True)
    class_room = models.CharField('班级', max_length=256, default=None, blank=True)

    # 7.第一部分
    part_1_1 = models.TextField('个人性格', max_length=256, default=None, blank=True)
    part_1_2 = models.TextField('兴趣爱好', max_length=256, default=None, blank=True)
    part_1_3 = models.TextField('自我评价', max_length=256, default=None, blank=True)

    part_2_1 = models.TextField('家人（父母、亲戚）评价', max_length=256, default=None, blank=True)
    part_2_2 = models.TextField('师长（老师、学长）评价', max_length=256, default=None, blank=True)
    part_2_3 = models.TextField('友人（同学、朋友）评价', max_length=256, default=None, blank=True)

    part_3_1 = models.TextField('个人评估总述', max_length=256, default=None, blank=True)
    part_3_2 = models.TextField('他人评估总述', max_length=256, default=None, blank=True)
    part_3_3 = models.TextField('从优缺点评价', max_length=256, default=None, blank=True)

    # 8.第二部分
    part_4_1 = models.TextField('家庭成员', max_length=256, default=None, blank=True)
    part_4_2 = models.TextField('家庭经济状况', max_length=256, default=None, blank=True)
    part_4_3 = models.TextField('家庭期望', max_length=256, default=None, blank=True)
    part_4_4 = models.TextField('家庭影响', max_length=256, default=None, blank=True)

    part_5_1 = models.TextField('组织环境分析', max_length=256, default=None, blank=True)
    part_5_2 = models.TextField('学院环境概况', max_length=256, default=None, blank=True)
    part_5_3 = models.TextField('整体就业环境分析', max_length=256, default=None, blank=True)
    part_5_4 = models.TextField('就业形势、毕业生规模、国家鼓励政策与制度', max_length=256, default=None, blank=True)
    part_5_5 = models.TextField('职业市场环境分析', max_length=256, default=None, blank=True)
    part_5_6 = models.TextField('中国市场概况、市场调查数据', max_length=256, default=None, blank=True)
    part_5_7 = models.TextField('自己的职业定位是符合环境现状', max_length=256, default=None, blank=True)

    # 9.第三部分
    part_6_1 = models.TextField('优势（Strength）', max_length=256, default=None, blank=True)
    part_6_2 = models.TextField('劣势（Weakness）', max_length=256, default=None, blank=True)
    part_6_3 = models.TextField('机会（Opportunity）', max_length=256, default=None, blank=True)
    part_6_4 = models.TextField('威胁（Threat）', max_length=256, default=None, blank=True)

    part_6_5 = models.TextField('如何利用自己的优势和机会改正弱势避免威胁？', max_length=256, default=None, blank=True)

    # 10.第四部分
    part_7_1 = models.TextField('准备期及备选方案', max_length=256, default=None, blank=True)
    part_7_2 = models.TextField('初期及备选方案', max_length=256, default=None, blank=True)
    part_7_3 = models.TextField('中期及备选方案', max_length=256, default=None, blank=True)
    part_7_4 = models.TextField('成熟期及备选方案', max_length=256, default=None, blank=True)
    part_7_5 = models.TextField('结束期及备选方案', max_length=256, default=None, blank=True)

    part_8_1 = models.TextField('准备期及备选方案', max_length=256, default=None, blank=True)
    part_8_2 = models.TextField('初期及备选方案', max_length=256, default=None, blank=True)
    part_8_3 = models.TextField('中期及备选方案', max_length=256, default=None, blank=True)
    part_8_4 = models.TextField('成熟期及备选方案', max_length=256, default=None, blank=True)
    part_8_5 = models.TextField('结束期及备选方案', max_length=256, default=None, blank=True)

    # 11.第五部分
    part_9_1 = models.TextField('我的职业生涯终极目标是', max_length=256, default=None, blank=True)
    part_9_2 = models.TextField('实现目标的途径和阶段分析', max_length=256, default=None, blank=True)
    # 准备
    part_10_1 = models.TextField('本阶段目标分解', max_length=256, default=None, blank=True)
    part_10_2 = models.TextField('实施策略', max_length=256, default=None, blank=True)
    part_10_3 = models.TextField('效果', max_length=256, default=None, blank=True)
    part_10_4 = models.TextField('方案', max_length=256, default=None, blank=True)
    part_10_5 = models.TextField('本阶段备选方案', max_length=256, default=None, blank=True)
    # 初期
    part_11_1 = models.TextField('本阶段目标分解', max_length=256, default=None, blank=True)
    part_11_2 = models.TextField('实施策略', max_length=256, default=None, blank=True)
    part_11_3 = models.TextField('效果', max_length=256, default=None, blank=True)
    part_11_4 = models.TextField('方案', max_length=256, default=None, blank=True)
    part_11_5 = models.TextField('本阶段备选方案', max_length=256, default=None, blank=True)
    # 中期
    part_12_1 = models.TextField('本阶段目标分解', max_length=256, default=None, blank=True)
    part_12_2 = models.TextField('实施策略', max_length=256, default=None, blank=True)
    part_12_3 = models.TextField('效果', max_length=256, default=None, blank=True)
    part_12_4 = models.TextField('方案', max_length=256, default=None, blank=True)
    part_12_5 = models.TextField('本阶段备选方案', max_length=256, default=None, blank=True)
    # 成熟
    part_13_1 = models.TextField('本阶段目标分解', max_length=256, default=None, blank=True)
    part_13_2 = models.TextField('实施策略', max_length=256, default=None, blank=True)
    part_13_3 = models.TextField('效果', max_length=256, default=None, blank=True)
    part_13_4 = models.TextField('方案', max_length=256, default=None, blank=True)
    part_13_5 = models.TextField('本阶段备选方案', max_length=256, default=None, blank=True)
    # 结束
    part_14_1 = models.TextField('本阶段目标分解', max_length=256, default=None, blank=True)
    part_14_2 = models.TextField('实施策略', max_length=256, default=None, blank=True)
    part_14_3 = models.TextField('效果', max_length=256, default=None, blank=True)
    part_14_4 = models.TextField('方案', max_length=256, default=None, blank=True)
    part_14_5 = models.TextField('本阶段备选方案', max_length=256, default=None, blank=True)

    # 12.第六部分
    part_15_1 = models.TextField('职业目标评估', max_length=256, default=None, blank=True)
    part_15_2 = models.TextField('职业路径评估', max_length=256, default=None, blank=True)
    part_15_3 = models.TextField('实施策略评估', max_length=256, default=None, blank=True)
    part_15_4 = models.TextField('其它因素评估', max_length=256, default=None, blank=True)

    part_16_1 = models.TextField('一般情况下，我定期（半年或一年）评估规划', max_length=256, default=None, blank=True)
    part_16_2 = models.TextField('补救措施', max_length=256, default=None, blank=True)
    part_16_3 = models.TextField('结束语', max_length=256, default=None, blank=True)
    part_16_4 = models.TextField('主要参考文献', max_length=256, default=None, blank=True)


class Disc(models.Model):
    user = models.CharField(verbose_name="yh", max_length=30, default="", null=True, blank=True)
    # user = models.OneToOneField(UserInfo, on_delete=models.CASCADE, null=True, blank=True)
    yi_choices = (  # 新建选择字段
        (1, '富于冒险:愿意面对新事物并敢于下决心掌握的人'),
        (3, '适应力强:轻松自如适应任何环境'),
        (2, '生动:充满活力,表情生动,多手势'),
        (4, '善于分析:喜欢研究各部分之间的逻辑和正确的关系'),
    )
    er_choices = (  # 新建选择字段
        (3, '坚持不懈：要完成现有的事才能做新的事情'),
        (2, '喜好娱乐：开心充满乐趣与幽默感'),
        (4, '善于说服：用逻辑和事实而不用威严和权利服人'),
        (1, '平和：在冲突中不受干扰，保持平静'),
    )
    san_choices = (  # 新建选择字段
        (4, '顺服：易接受他人的观点和喜好，不坚持己见'),
        (3, '自我牺牲：为他人利益愿意放弃个人意见'),
        (1, '善于社交：认为与人相处是好玩，而不是挑战或者商业机会'),
        (2, '意志坚定：决心以自己的方式做事'),
    )
    si_choices = (  # 新建选择字段
        (3, '使人认同：因人格魅力或性格使人认同'),
        (1, '体贴：关心别人的感受与需要'),
        (4, '竞争性：把一切当作竞赛，总是有强烈的赢的欲望'),
        (2, '自控性：控制自己的情感，极少流露'),
    )
    wu_choices = (  # 新建选择字段
        (3, '使人振作：给他人清新振奋的刺激'),
        (1, '尊重他人：对人诚实尊重'),
        (4, '善于应变：对任何情况都能作出有效的反应'),
        (2, '含蓄：自我约束情绪与热忱'),
    )
    liu_choices = (  # 新建选择字段
        (4, '生机勃勃：充满生命力与兴奋'),
        (1, '满足：容易接受任何情况与环境'),
        (2, '敏感：对周围的人事过分关心'),
        (3, '自立：独立性强，只依靠自己的能力、判断、与才智'),
    )
    qi_choices = (  # 新建选择字段
        (3, '计划者：先做详尽的计划，并严格要计划进行，不想改动'),
        (4, '耐性：不因延误而懊恼，冷静且能容忍'),
        (2, '积极：相信自己有转危为安的能力'),
        (1, '推动者：动用性格魅力或鼓励别人参与'),
    )
    ba_choices = (  # 新建选择字段
        (1, '肯定：自信，极少犹豫或者动摇'),
        (2, '无拘无束：不喜欢预先计划，或者被计划牵制'),
        (3, '羞涩：安静，不善于交谈'),
        (4, '有时间性：生活处事依靠时间表，不喜欢计划被人干扰'),
    )
    jiu_choices = (  # 新建选择字段
        (4, '迁就：改变自己以与他人协调，短时间内按他人要求行事'),
        (3, '井井有条：有系统有条理安排事情的人'),
        (1, '坦率：毫无保留，坦率发言'),
        (2, '乐观：令他人和自己相信任何事情都会好转'),
    )
    shi_choices = (  # 新建选择字段
        (1, '强迫性：发号施令，强迫他人听从'),
        (3, '忠诚：一贯可靠，忠心不移，有时毫无根据地奉献'),
        (4, '有趣：风趣，幽默，把任何事物都能变成精彩的故事'),
        (2, '友善：不主动交谈，不爱争论'),
    )
    shiyi_choices = (  # 新建选择字段
        (1, '勇敢：敢于冒险，无所畏惧'),
        (4, '体贴：待人得体，有耐心'),
        (2, '注意细节：观察入微，做事情有条不紊'),
        (3, '可爱：开心，与他人相处充满乐趣'),
    )
    shier_choices = (  # 新建选择字段
        (3, '令人开心：充满活力，并将快乐传于他人'),
        (1, '文化修养：对艺术学术特别爱好，如戏剧、交响乐'),
        (4, '自信：确信自己个人能力与成功'),
        (2, '贯彻始终：情绪平稳，做事情坚持不懈'),
    )
    shisan_choices = (  # 新建选择字段
        (2, '理想主义：以自己完美的标准来设想衡量新事物'),
        (4, '独立：自给自足，独立自信，不需要他人帮忙'),
        (3, '无攻击性：不说或者做可能引起别人不满和反对的事情'),
        (1, '富有激励：鼓励别人参与、加入，并把每件事情变得有趣'),
    )
    shisi_choices = (  # 新建选择字段
        (3, '感情外露：从不掩饰情感.喜好,交谈时常身不由己接触他人'),
        (1, '深沉：深刻并常常内省，对肤浅的交谈、消遣会厌恶'),
        (4, '果断：有很快做出判断与结论的能力'),
        (2, '幽默：语气平和而有冷静的幽默'),
    )
    shiwu_choices = (  # 新建选择字段
        (3, '调解者：经常居中调节不同的意见，以避免双方的冲突'),
        (4, '音乐性：爱好参与并有较深的鉴赏能力，因音乐的艺术性,而不是因为表演的乐趣'),
        (1, '发起人：高效率的推动者，是他人的领导者，闲不住'),
        (2, '喜交朋友：喜欢周旋聚会中，善交新朋友不把任何人当陌生人'),
    )
    shiliu_choices = (  # 新建选择字段
        (2, '考虑周到：善解人意，帮助别人，记住特别的日子'),
        (3, '执着：不达目的，誓不罢休'),
        (4, '多言：不断的说话、讲笑话以娱乐他人，觉得应该避免沉默而带来的的尴尬'),
        (1, '容忍：易接受别人的想法和看法，不需要反对或改变他人'),
    )
    shiqi_choices = (  # 新建选择字段
        (3, '聆听者：愿意听别人倾诉'),
        (4, '忠心对自己的理想、朋友、工作都绝对忠实，有时甚至不需要理由'),
        (1, '领导者：天生的领导，不相信别人的能力能比上自己'),
        (2, '活力充沛：充满活力，精力充沛'),
    )
    shiba_choices = (  # 新建选择字段
        (2, '知足：满足自己拥有的，很少羡慕别人'),
        (4, '首领：要求领导地位及别人跟随'),
        (1, '制图者：用图表数字来组织生活，解决问题'),
        (3, '惹人喜爱：人们注意的中心，令人喜欢'),
    )
    shijiu_choices = (  # 新建选择字段
        (3, '完美主义者：对自己、对别人都高标准、一切事物有秩序'),
        (4, '和气：易相处，易说话，易让人接近'),
        (2, '勤劳：不停的工作，完成任务，不愿意休息'),
        (1, '受欢迎：聚会时的灵魂人物，受欢迎的宾客'),
    )

    ershi_choices = (  # 新建选择字段
        (2, '跳跃性：充满活力和生气勃勃'),
        (1, '无畏：大胆前进，不怕冒险'),
        (4, '规范性：时时坚持自己的举止合乎认同的道德规范'),
        (3, '平衡：稳定，走中间路线'),
    )
    ershiyi_choices = (  # 新建选择字段
        (4, '乏味：死气沉沉，缺乏生气'),
        (3, '忸怩：躲避别人的注意力，在众人注意下不自然'),
        (1, '露骨：好表现，华而不实，声音大'),
        (2, '专横：喜命令支配，有时略显傲慢'),
    )
    ershier_choices = (  # 新建选择字段
        (2, '散漫：生活任性无秩序'),
        (1, '无同情心：不易理解别人的问题和麻烦'),
        (3, '缺乏热情：不易兴奋，经常感到好事难做'),
        (4, '不宽恕：不易宽恕和忘记别人对自己的伤害，易嫉妒'),
    )
    ershisan_choices = (  # 新建选择字段
        (3, '保留：不愿意参与，尤其是当事情复杂时'),
        (4, '怨恨：把实际或者自己想象的别人的冒犯经常放在心中'),
        (1, '逆反：抗拒、或者拒不接受别人的方法，固执己见'),
        (2, '唠叨：重复讲同一件事情或故事，忘记已经重复多次，总是不断找话题说话'),
    )
    ershisi_choices = (  # 新建选择字段
        (4, '挑剔：坚持琐事细节，总喜欢挑不足'),
        (3, '胆小：经常感到强烈的担心焦虑、悲戚'),
        (2, '健忘：缺乏自我约束，导致健忘，不愿意回忆无趣的事情'),
        (1, '率直：直言不讳，直接表达自己的看法'),
    )
    ershiwu_choices = (  # 新建选择字段
        (1, '没耐性：难以忍受等待别人'),
        (4, '无安全感：感到担心且无自信心'),
        (2, '优柔寡断：很难下决定'),
        (3, '好插嘴：一个滔滔不绝的发言人，不是好听众，不注意别人的说话'),
    )
    ershiliu_choices = (  # 新建选择字段
        (4, '不受欢迎：由于强烈要求完美，而拒人千里'),
        (3, '不参与：不愿意加入，不参与，对别人生活不感兴趣'),
        (2, '难预测：时而兴奋，时而低落，或总是不兑现诺言'),
        (1, '缺同情心：很难当众表达对弱者或者受难者的情感'),
    )
    ershiqi_choices = (  # 新建选择字段
        (1, '固执：坚持照自己的意见行事，不听不同意见'),
        (2, '随兴：做事情没有一贯性，随意做事情'),
        (4, '难于取悦：因为要求太高而使别人很难取悦'),
        (3, '行动迟缓：迟迟才行动，不易参与或者行动总是慢半拍'),
    )
    ershiba_choices = (  # 新建选择字段
        (3, '平淡：平实淡漠，中间路线,无高低之分，很少表露情感'),
        (4, '悲观：尽管期待最好但往往首先看到事物不利之处'),
        (1, '自负：自我评价高，认为自己是最好的人选'),
        (2, '放任:许别人做他喜欢做的事情，为的是讨好别人，令别人鼓吹自己'),
    )
    ershijiu_choices = (  # 新建选择字段
        (3, '易怒：善变，孩子性格，易激动，过后马上就忘了'),
        (1, '无目标：不喜欢目标，也无意订目标'),
        (2, '好争论：易与人争吵，不管对何事都觉得自己是对的'),
        (4, '孤芳自赏：容易感到被疏离，经常没有安全感或担心别人不喜欢和自己相处'),
    )
    sanshi_choices = (  # 新建选择字段
        (3, '天真：孩子般的单纯，不理解生命的真谛'),
        (1, '消极：往往看到事物的消极面阴暗面，而少有积极的态度'),
        (4, '鲁莽：充满自信有胆识但总是不恰当'),
        (2, '冷漠：漠不关心，得过且过'),
    )
    sanshiyi_choices = (  # 新建选择字段
        (3, '担忧：时时感到不确定、焦虑、心烦'),
        (4, '不善交际:总喜欢挑人毛病，不被人喜欢'),
        (1, '工作狂:为了回报或者说成就感，而不是为了完美，因而设立雄伟目标不断工作，耻于休息'),
        (2, '喜获认同：需要旁人认同赞赏，像演员'),
    )
    sanshier_choices = (  # 新建选择字段
        (2, '过分敏感：对事物过分反应，被人误解时感到被冒犯'),
        (4, '不圆滑老练：经常用冒犯或考虑不周的方式表达自己'),
        (3, '胆怯：遇到困难退缩'),
        (2, '喋喋不休：难以自控，滔滔不绝，不能倾听别人'),
    )
    sanshisan_choices = (  # 新建选择字段
        (3, '腼腆：事事不确定，对所做的事情缺乏信心'),
        (2, '生活紊乱：缺乏安排生活的能力'),
        (1, '跋扈：冲动的控制事物和别人，指挥他人'),
        (4, '抑郁：常常情绪低落'),
    )
    sanshisi_choices = (  # 新建选择字段
        (3, '缺乏毅力：反复无常，互相矛盾，情绪与行动不合逻辑'),
        (1, '内向：活在自己的世界里，思想和兴趣放在心里'),
        (4, '不容忍：不能忍受他人的观点、态度和做事的方式'),
        (2, '无异议：对很多事情漠不关心'),
    )
    sanshiwu_choices = (  # 新建选择字段
        (4, '杂乱无章：生活环境无秩序，经常找不到东西'),
        (1, '情绪化：情绪不易高涨，感到不被欣赏时很容易低落'),
        (3, '喃喃自语：低声说话，不在乎说不清楚'),
        (2, '喜操纵：精明处事，操纵事情，使对自己有利'),
    )
    sanshiliu_choices = (  # 新建选择字段
        (2, '缓慢：行动思想均比较慢，过分麻烦'),
        (3, '顽固：决心依自己的意愿行事，不易被说服'),
        (1, '好表现：要吸引人，需要自己成为被人注意的中心'),
        (4, '有戒心：不易相信，对语言背后的真正的动机存在疑问'),
    )
    sanshiqi_choices = (  # 新建选择字段
        (2, '孤僻：需要大量的时间独处，避开人群'),
        (4, '统治欲：毫不犹豫地表示自己的正确或控制能力'),
        (3, '懒惰：总是先估量事情要耗费多少精力，能不做最好'),
        (1, '大嗓门：说话声和笑声总盖过他人'),
    )
    sanshiba_choices = (  # 新建选择字段
        (3, '拖延：凡事起步慢，需要推动力'),
        (4, '多疑：凡事怀疑，不相信别人'),
        (1, '易怒：对行动不快或不能完成指定工作时易烦躁和发怒'),
        (2, '不专注：无法专心致志或者集中精力'),
    )
    sanshijiu_choices = (  # 新建选择字段
        (4, '报复性：记恨并惩罚冒犯自己的人'),
        (2, '烦躁：喜新厌旧，不喜欢长时间做相同的事情'),
        (3, '勉强：不愿意参与或者说投入'),
        (1, '轻率：因没有耐心，不经思考，草率行动'),
    )
    sishi_choices = (  # 新建选择字段
        (3, '妥协：为避免矛盾即使自己是对的也不惜放弃自己的立场'),
        (4, '好批评：不断地衡量和下判断，经常考虑提出反对意见'),
        (1, '狡猾：精明，总是有办法达到目的'),
        (2, '善变：像孩子般注意力短暂，需要各种变化，怕无聊'),
    )
    yi = models.SmallIntegerField(verbose_name="第一题", choices=yi_choices)
    er = models.SmallIntegerField(verbose_name="第二题", choices=er_choices)
    san = models.SmallIntegerField(verbose_name="第三题", choices=san_choices)
    si = models.SmallIntegerField(verbose_name="第四题", choices=si_choices)
    wu = models.SmallIntegerField(verbose_name="第五题", choices=wu_choices)
    liu = models.SmallIntegerField(verbose_name="第六题", choices=liu_choices)
    qi = models.SmallIntegerField(verbose_name="第七题", choices=qi_choices)
    ba = models.SmallIntegerField(verbose_name="第八题", choices=ba_choices)
    jiu = models.SmallIntegerField(verbose_name="第九题", choices=jiu_choices)
    shi = models.SmallIntegerField(verbose_name="第十题", choices=shi_choices)
    shiyi = models.SmallIntegerField(verbose_name="第十一题", choices=shiyi_choices)
    shier = models.SmallIntegerField(verbose_name="第十二题", choices=shier_choices)
    shisan = models.SmallIntegerField(verbose_name="第十三题", choices=shisan_choices)
    shisi = models.SmallIntegerField(verbose_name="第十四题", choices=shisi_choices)
    shiwu = models.SmallIntegerField(verbose_name="第十五题", choices=shiwu_choices)
    shiliu = models.SmallIntegerField(verbose_name="第十六题", choices=shiliu_choices)
    shiqi = models.SmallIntegerField(verbose_name="第十七题", choices=shiqi_choices)
    shiba = models.SmallIntegerField(verbose_name="第十八题", choices=shiba_choices)
    shijiu = models.SmallIntegerField(verbose_name="第十九题", choices=shijiu_choices)
    ershi = models.SmallIntegerField(verbose_name="第二十题", choices=ershi_choices)
    ershiyi = models.SmallIntegerField(verbose_name="第二十一题", choices=ershiyi_choices)
    ershier = models.SmallIntegerField(verbose_name="第二十二题", choices=ershier_choices)
    ershisan = models.SmallIntegerField(verbose_name="第二十三题", choices=ershisan_choices)
    ershisi = models.SmallIntegerField(verbose_name="第二十四题", choices=ershisi_choices)
    ershiwu = models.SmallIntegerField(verbose_name="第二十五题", choices=ershiwu_choices)
    ershiliu = models.SmallIntegerField(verbose_name="第二十六题", choices=ershiliu_choices)
    ershiqi = models.SmallIntegerField(verbose_name="第二十七题", choices=ershiqi_choices)
    ershiba = models.SmallIntegerField(verbose_name="第二十八题", choices=ershiba_choices)
    ershijiu = models.SmallIntegerField(verbose_name="第二十九题", choices=ershijiu_choices)
    sanshi = models.SmallIntegerField(verbose_name="第三十题", choices=sanshi_choices)
    sanshiyi = models.SmallIntegerField(verbose_name="第三十一题", choices=sanshiyi_choices)
    sanshier = models.SmallIntegerField(verbose_name="第三十二题", choices=sanshier_choices)
    sanshisan = models.SmallIntegerField(verbose_name="第三十三题", choices=sanshisan_choices)
    sanshisi = models.SmallIntegerField(verbose_name="第三十四题", choices=sanshisi_choices)
    sanshiwu = models.SmallIntegerField(verbose_name="第三十五题", choices=sanshiwu_choices)
    sanshiliu = models.SmallIntegerField(verbose_name="第三十六题", choices=sanshiliu_choices)
    sanshiqi = models.SmallIntegerField(verbose_name="第三十七题", choices=sanshiqi_choices)
    sanshiba = models.SmallIntegerField(verbose_name="第三十八题", choices=sanshiba_choices)
    sanshijiu = models.SmallIntegerField(verbose_name="第三十九题", choices=sanshijiu_choices)
    sishi = models.SmallIntegerField(verbose_name="第四十题", choices=sishi_choices)


# E  I  S  N  T  F  J  P
# 1  2  3  4  5  6  7  8
class Mbti(models.Model):
    # user = models.OneToOneField(UserInfo, on_delete=models.CASCADE, null=True, blank=True)
    user = models.CharField(verbose_name="yh", max_length=30, default="", null=True, blank=True)
    Mbtiyi_choices = (  # 新建选择字段
        (7, "J计划你要做什么和在什么时候做"),
        (8, 'P说去就去'),
    )
    Mbtier_choices = (  # 新建选择字段
        (8, 'P较为随兴所至的人'),
        (7, 'J较为有条理的人'),
    )
    Mbtisan_choices = (  # 新建选择字段
        (3, 'S以事实为主的课程'),
        (4, 'N涉及理论的课程'),
    )
    Mbtisi_choices = (  # 新建选择字段
        (1, 'E与人容易混熟'),
        (2, 'I比较沉静或矜持'),
    )
    Mbtiwu_choices = (  # 新建选择字段
        (4, 'N富于想象力的人'),
        (3, 'S现实的人'),
    )
    Mbtiliu_choices = (  # 新建选择字段
        (6, 'F你的情感支配你的理智'),
        (5, 'T你的理智主宰你的情感'),
    )
    Mbtiqi_choices = (  # 新建选择字段
        (8, 'P凭兴所至行事'),
        (7, 'J按照计划行事'),
    )
    Mbtiba_choices = (  # 新建选择字段
        (1, 'E容易让人了解'),
        (2, 'I难于让人了解'),
    )
    Mbtijiu_choices = (  # 新建选择字段
        (7, 'J合你心意'),
        (8, 'P令你感到束缚'),
    )
    Mbtishi_choices = (  # 新建选择字段
        (7, 'J开始前小心组织计划'),
        (8, 'P边做边找须做什么'),
    )
    Mbtishiyi_choices = (  # 新建选择字段
        (8, 'P顺其自然'),
        (7, 'J按程序表做事'),
    )
    Mbtishier_choices = (  # 新建选择字段
        (2, 'I重视自我隐私的人'),
        (1, 'E非常坦率开放的人'),
    )
    Mbtishisan_choices = (  # 新建选择字段
        (3, 'S实事求是的人'),
        (4, 'N机灵的人'),
    )
    Mbtishisi_choices = (  # 新建选择字段
        (1, 'E你介绍大家认识'),
        (2, 'I别人介绍你'),
    )
    Mbtishiwu_choices = (  # 新建选择字段
        (4, 'N常提出新注意的'),
        (3, 'S脚踏实地的'),
    )
    Mbtishiliu_choices = (  # 新建选择字段
        (6, 'F重视感情多于逻辑'),
        (5, 'T重视逻辑多于感情'),
    )
    Mbtishiqi_choices = (  # 新建选择字段
        (8, 'P坐观事情发展才作计划'),
        (7, 'J很早就作计划'),
    )
    Mbtishiba_choices = (  # 新建选择字段
        (2, 'I一个人独处'),
        (1, 'E合别人在一起'),
    )
    Mbtishijiu_choices = (  # 新建选择字段
        (1, 'E令你活力培增'),
        (2, 'I常常令你心力憔悴'),
    )
    Mbtiershi_choices = (  # 新建选择字段
        (7, 'J很早便把约会、社交聚集等事情安排妥当'),
        (8, 'P无拘无束，看当时有什么好玩就做什么'),
    )
    Mbtiershiyi_choices = (  # 新建选择字段
        (8, 'P大部分的时间都是跟当天的感觉行事'),
        (7, 'J事先知道大部分的日子会做什么'),
    )
    Mbtiershier_choices = (  # 新建选择字段
        (2, 'I有时感到郁闷'),
        (1, 'E常常乐在其中'),
    )
    Mbtiershisan_choices = (  # 新建选择字段
        (1, 'E和别人容易混熟'),
        (2, 'I趋向自处一隅'),
    )
    Mbtiershisi_choices = (  # 新建选择字段
        (4, 'N一个思想敏捷及非常聪颖的人'),
        (3, 'S实事求是，具丰富常识的人'),
    )
    Mbtiershiwu_choices = (  # 新建选择字段
        (8, 'P颇为喜欢处理迫使你分秒必争的突发'),
        (7, 'J通常预先计划，以免要在压力下工作'),
    )

    Mbtiershiliu_choices = (  # 新建选择字段
        (2, 'I要花很长时间才认识你'),
        (1, 'E用很短的时间便认识你'),
    )
    Mbtiershiqi_choices = (  # 新建选择字段
        (2, 'I注重隐私'),
        (1, 'E坦率开放'),
    )
    Mbtiershiba_choices = (  # 新建选择字段
        (7, 'J预先安排的'),
        (8, 'P无计划的'),
    )
    Mbtiershijiu_choices = (  # 新建选择字段
        (4, 'N抽象'),
        (3, 'S具体'),
    )
    Mbtisanshi_choices = (  # 新建选择字段
        (6, 'F温柔'),
        (5, 'T坚定'),
    )
    Mbtisanshiyi_choices = (  # 新建选择字段
        (5, 'T思考'),
        (6, 'F感受'),
    )
    Mbtisanshier_choices = (  # 新建选择字段
        (3, 'S事实'),
        (4, 'N意念'),
    )
    Mbtisanshisan_choices = (  # 新建选择字段
        (8, 'P冲动'),
        (7, 'J决定'),
    )
    Mbtisanshisi_choices = (  # 新建选择字段
        (1, 'E热衷'),
        (2, 'I文静'),
    )
    Mbtisanshiwu_choices = (  # 新建选择字段
        (2, 'I文静'),
        (1, 'E外向'),
    )
    Mbtisanshiliu_choices = (  # 新建选择字段
        (7, 'J有系统'),
        (8, 'P随意'),
    )
    Mbtisanshiqi_choices = (  # 新建选择字段
        (4, 'N理论'),
        (3, 'S肯定'),
    )
    Mbtisanshiba_choices = (  # 新建选择字段
        (6, 'F敏感'),
        (5, 'T公正'),
    )
    Mbtisanshijiu_choices = (  # 新建选择字段
        (5, 'T令人信服'),
        (6, 'F感人的'),
    )
    Mbtisishi_choices = (  # 新建选择字段
        (3, 'S声明'),
        (4, 'N概念'),
    )
    Mbtisishiyi_choices = (  # 新建选择字段
        (8, 'P不受约束'),
        (7, 'J预先安排'),
    )
    Mbtisishier_choices = (  # 新建选择字段
        (2, 'I矜持'),
        (1, 'E健谈'),
    )
    Mbtisishisan_choices = (  # 新建选择字段
        (7, 'J有条不紊'),
        (8, 'P不拘小节'),
    )
    Mbtisishisi_choices = (  # 新建选择字段
        (4, 'N意念'),
        (3, 'S实况'),
    )
    Mbtisishiwu_choices = (  # 新建选择字段
        (6, 'F同情怜悯'),
        (5, 'T远见'),
    )
    Mbtisishiliu_choices = (  # 新建选择字段
        (5, 'T利益'),
        (6, 'F祝福'),
    )
    Mbtisishiqi_choices = (  # 新建选择字段
        (3, 'S务实的'),
        (4, 'N理论的'),
    )
    Mbtisishiba_choices = (  # 新建选择字段
        (2, 'I朋友不多'),
        (1, 'E朋友众多'),
    )
    Mbtisishijiu_choices = (  # 新建选择字段
        (7, 'J有系统'),
        (8, 'P即兴'),
    )
    Mbtiwushi_choices = (  # 新建选择字段
        (4, 'N富想象的'),
        (3, 'S以事论事'),
    )
    Mbtiwushiyi_choices = (  # 新建选择字段
        (6, 'F亲切的'),
        (5, 'T客观的'),
    )
    Mbtiwushier_choices = (  # 新建选择字段
        (5, 'T客观的'),
        (6, 'F热情的'),
    )
    Mbtiwushisan_choices = (  # 新建选择字段
        (3, 'S建造'),
        (4, 'N发明'),
    )
    Mbtiwushisi_choices = (  # 新建选择字段
        (2, 'I文静'),
        (1, 'E爱合群'),
    )
    Mbtiwushiwu_choices = (  # 新建选择字段
        (4, 'N理论'),
        (3, 'S事实'),
    )
    Mbtiwushiliu_choices = (  # 新建选择字段
        (6, 'F富同情'),
        (5, 'T合逻辑'),
    )
    Mbtiwushiqi_choices = (  # 新建选择字段
        (5, 'T具分析力'),
        (6, 'F多愁善感'),
    )
    Mbtiwushiba_choices = (  # 新建选择字段
        (3, 'S合情合理'),
        (4, 'N令人着迷'),
    )
    Mbtiwushijiu_choices = (  # 新建选择字段
        (7, 'J把要做的不同工作依次列出'),
        (8, 'P马上动工'),
    )
    Mbtiliushi_choices = (  # 新建选择字段
        (2, 'I与某些人很难打开话匣儿和保持对话'),
        (1, 'E与多数人都能从容地长谈'),
    )
    Mbtiliushiyi_choices = (  # 新建选择字段
        (3, 'S按照一般认可的方法去做'),
        (4, 'N构想一个自己的想法'),
    )
    Mbtiliushier_choices = (  # 新建选择字段
        (1, 'E马上可以'),
        (2, 'I要待他们真正了解你之后才可以'),
    )
    Mbtiliushisan_choices = (  # 新建选择字段
        (4, 'N讲授概念和原则的'),
        (3, 'S讲授事实和数据的'),
    )
    Mbtiliushisi_choices = (  # 新建选择字段
        (6, 'F一贯感性的人'),
        (5, 'T一贯理性的人'),
    )
    Mbtiliushiwu_choices = (  # 新建选择字段
        (8, 'P有时是需要的，但一般来说你不大喜欢这样做'),
        (7, 'J大多数情况下是有帮助而且是你喜欢做的'),
    )
    Mbtiliushiliu_choices = (  # 新建选择字段
        (2, 'I跟你很熟悉的个别人谈话'),
        (1, 'E参与大伙的谈话'),
    )
    Mbtiliushiqi_choices = (  # 新建选择字段
        (1, 'E是说话很多的一个'),
        (2, 'I让别人多说话'),
    )
    Mbtiliushiba_choices = (  # 新建选择字段
        (7, 'J合你意'),
        (8, 'P使你提不起劲'),
    )
    Mbtiliushijiu_choices = (  # 新建选择字段
        (5, 'T能干的'),
        (6, 'F富有同情心'),
    )
    Mbtiqishi_choices = (  # 新建选择字段
        (7, 'J事先安排你的社交约会'),
        (8, 'P随兴之所至做事'),
    )
    Mbtiqishiyi_choices = (  # 新建选择字段
        (8, 'P边做边想该做什么'),
        (7, 'J首先把工作按步细分'),
    )
    Mbtiqishier_choices = (  # 新建选择字段
        (2, 'I只限于跟你有共同兴趣的人'),
        (1, 'E几乎跟任何人都可以'),
    )
    Mbtiqishisan_choices = (  # 新建选择字段
        (3, 'S跟随一些证明有效的方法'),
        (4, 'N分析还有什么毛病，及针对尚未解决的难题'),
    )
    Mbtiqishisi_choices = (  # 新建选择字段
        (4, 'N喜欢奇特或创新的表达方式'),
        (3, 'S喜欢作者直话直说'),
    )
    Mbtiqishiwu_choices = (  # 新建选择字段
        (5, 'T天性淳良，但常常前后不一的'),
        (4, 'N言词尖锐但永远合乎逻辑的'),
    )
    Mbtiqishiliu_choices = (  # 新建选择字段
        (8, 'P按当天心情去做'),
        (7, 'J照拟好的程序表去做'),
    )
    Mbtiqishiqi_choices = (  # 新建选择字段
        (1, 'E可以和任何人按需求从容地交谈'),
        (2, 'I只是对某些人或在某种情况下才可以畅所欲言'),
    )
    Mbtiqishiba_choices = (  # 新建选择字段
        (5, 'T据事实衡量'),
        (6, 'F考虑他人的感受和意见'),
    )
    Mbtiqishijiu_choices = (  # 新建选择字段
        (4, 'N想象的'),
        (3, 'S真实的'),
    )
    Mbtibashi_choices = (  # 新建选择字段
        (6, 'F仁慈慷慨的'),
        (5, 'T意志坚定的'),
    )
    Mbtibashiyi_choices = (  # 新建选择字段
        (5, 'T公正的'),
        (6, 'F有关怀心'),
    )
    Mbtibashier_choices = (  # 新建选择字段
        (3, 'S制作'),
        (4, 'N设计'),
    )
    Mbtibashisan_choices = (  # 新建选择字段
        (4, 'N可能性'),
        (3, 'S必然性'),
    )
    Mbtibashisi_choices = (  # 新建选择字段
        (6, 'F温柔'),
        (5, 'T力量'),
    )
    Mbtibashiwu_choices = (  # 新建选择字段
        (5, 'T实际'),
        (6, 'F多愁善感'),
    )
    Mbtibashiliu_choices = (  # 新建选择字段
        (3, 'S制造'),
        (4, 'N创造'),
    )
    Mbtibashiqi_choices = (  # 新建选择字段
        (4, 'N新颖的'),
        (3, 'S已知的'),
    )
    Mbtibashiba_choices = (  # 新建选择字段
        (6, 'F同情'),
        (5, 'T分析'),
    )
    Mbtibashijiu_choices = (  # 新建选择字段
        (5, 'T坚持己见'),
        (6, 'F温柔有爱心'),
    )
    Mbtijiushi_choices = (  # 新建选择字段
        (3, 'S具体的'),
        (4, 'N抽象的'),
    )
    Mbtijiushiyi_choices = (  # 新建选择字段
        (6, 'F全心投入'),
        (5, 'T有决心的'),
    )
    Mbtijiushier_choices = (  # 新建选择字段
        (5, 'T能干'),
        (6, 'F仁慈'),
    )
    Mbtijiushisan_choices = (  # 新建选择字段
        (3, 'S实际'),
        (4, 'N创新'),
    )
    yi = models.SmallIntegerField(verbose_name="当你要外出一整天，你会", choices=Mbtiyi_choices)
    er = models.SmallIntegerField(verbose_name="你认为自己是一个", choices=Mbtier_choices)
    san = models.SmallIntegerField(verbose_name="假如你是一位老师，你会选教", choices=Mbtisan_choices)
    si = models.SmallIntegerField(verbose_name="你通常", choices=Mbtisi_choices)
    wu = models.SmallIntegerField(verbose_name="一般来说，你和哪些人比较合得来？", choices=Mbtiwu_choices)
    liu = models.SmallIntegerField(verbose_name="你是否经常让", choices=Mbtiliu_choices)
    qi = models.SmallIntegerField(verbose_name="处理许多事情上，你会喜欢", choices=Mbtiqi_choices)
    ba = models.SmallIntegerField(verbose_name="你是否", choices=Mbtiba_choices)
    jiu = models.SmallIntegerField(verbose_name="按照程序表做事", choices=Mbtijiu_choices)
    shi = models.SmallIntegerField(verbose_name="当你有一份特别的任务，你会喜欢", choices=Mbtishi_choices)
    shiyi = models.SmallIntegerField(verbose_name="在大多数情况下，你会选择", choices=Mbtishiyi_choices)
    shier = models.SmallIntegerField(verbose_name="大多数人会说你是一个", choices=Mbtishier_choices)
    shisan = models.SmallIntegerField(verbose_name="你宁愿被人认为是一个", choices=Mbtishisan_choices)
    shisi = models.SmallIntegerField(verbose_name="在一大群人当中，通常是", choices=Mbtishisi_choices)
    shiwu = models.SmallIntegerField(verbose_name="你会跟哪些人做朋友", choices=Mbtishiwu_choices)
    shiliu = models.SmallIntegerField(verbose_name="你倾向", choices=Mbtishiliu_choices)
    shiqi = models.SmallIntegerField(verbose_name="你比较喜欢", choices=Mbtishiqi_choices)
    shiba = models.SmallIntegerField(verbose_name="你喜欢花很多的时间", choices=Mbtishiba_choices)
    shijiu = models.SmallIntegerField(verbose_name="与很多人一起会", choices=Mbtishijiu_choices)
    ershi = models.SmallIntegerField(verbose_name="你比较喜欢", choices=Mbtiershi_choices)
    ershiyi = models.SmallIntegerField(verbose_name="计划一个旅程时，你较喜欢", choices=Mbtiershiyi_choices)
    ershier = models.SmallIntegerField(verbose_name="在社交聚会中，你", choices=Mbtiershier_choices)
    ershisan = models.SmallIntegerField(verbose_name="你通常", choices=Mbtiershisan_choices)
    ershisi = models.SmallIntegerField(verbose_name="哪些人会更吸引你？", choices=Mbtiershisi_choices)
    ershiwu = models.SmallIntegerField(verbose_name="在日常工作中，你会", choices=Mbtiershiwu_choices)
    ershiliu = models.SmallIntegerField(verbose_name="你认为别人一般", choices=Mbtiershiliu_choices)
    ershiqi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiershiqi_choices)
    ershiba = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiershiba_choices)
    ershijiu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiershijiu_choices)
    sanshi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshi_choices)
    sanshiyi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshiyi_choices)
    sanshier = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshier_choices)
    sanshisan = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshisan_choices)
    sanshisi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshisi_choices)
    sanshiwu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshiwu_choices)
    sanshiliu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshiliu_choices)
    sanshiqi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshiqi_choices)
    sanshiba = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshiba_choices)
    sanshijiu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisanshijiu_choices)
    sishi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishi_choices)
    sishiyi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishiyi_choices)
    sishier = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishier_choices)
    sishisan = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishisan_choices)
    sishisi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishisi_choices)
    sishiwu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishiwu_choices)
    sishiliu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishiliu_choices)
    sishiqi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishiqi_choices)
    sishiba = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishiba_choices)
    sishijiu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtisishijiu_choices)
    wushi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushi_choices)
    wushiyi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushiyi_choices)
    wushier = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushier_choices)
    wushisan = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushisan_choices)
    wushisi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushisi_choices)
    wushiwu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushiwu_choices)
    wushiliu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushiliu_choices)
    wushiqi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushiqi_choices)
    wushiba = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiwushiba_choices)
    wushijiu = models.SmallIntegerField(verbose_name="当你要在一个星期内完成一个大项目，你在开始的时候会", choices=Mbtiwushijiu_choices)
    liushi = models.SmallIntegerField(verbose_name="在社交场合中，你经常会感到", choices=Mbtiliushi_choices)
    liushiyi = models.SmallIntegerField(verbose_name="要做许多人也做的事，你比较喜欢", choices=Mbtiliushiyi_choices)
    liushier = models.SmallIntegerField(verbose_name="你刚认识的朋友能否说出你的兴趣", choices=Mbtiliushier_choices)
    liushisan = models.SmallIntegerField(verbose_name="你通常较喜欢的科目是", choices=Mbtiliushisan_choices)
    liushisi = models.SmallIntegerField(verbose_name="哪个是较高的赞誉，或称许为", choices=Mbtiliushisi_choices)
    liushiwu = models.SmallIntegerField(verbose_name="你认为按照程序表做事", choices=Mbtiliushiwu_choices)
    liushiliu = models.SmallIntegerField(verbose_name="和一群人在一起，你通常会选", choices=Mbtiliushiliu_choices)
    liushiqi = models.SmallIntegerField(verbose_name="在社交聚会上，你会", choices=Mbtiliushiqi_choices)
    liushiba = models.SmallIntegerField(verbose_name="把周末期间要完成的事列成清单，这个主意会", choices=Mbtiliushiba_choices)
    liushijiu = models.SmallIntegerField(verbose_name="哪个是较高的赞誉，或称许为", choices=Mbtiliushijiu_choices)
    qishi = models.SmallIntegerField(verbose_name="你通常喜欢", choices=Mbtiqishi_choices)
    qishiyi = models.SmallIntegerField(verbose_name="总的说来，要做一个大型作业时，你会选", choices=Mbtiqishiyi_choices)
    qishier = models.SmallIntegerField(verbose_name="你能否滔滔不绝地与人聊天", choices=Mbtiqishier_choices)
    qishisan = models.SmallIntegerField(verbose_name="你会", choices=Mbtiqishisan_choices)
    qishisi = models.SmallIntegerField(verbose_name="为乐趣而阅读时，你会", choices=Mbtiqishisi_choices)
    qishiwu = models.SmallIntegerField(verbose_name="你宁愿替哪一类上司（或者老师）工作？", choices=Mbtiqishiwu_choices)
    qishiliu = models.SmallIntegerField(verbose_name="你做事多数是", choices=Mbtiqishiliu_choices)
    qishiqi = models.SmallIntegerField(verbose_name="你是否", choices=Mbtiqishiqi_choices)
    qishiba = models.SmallIntegerField(verbose_name="要作决定时，你认为比较重要的是", choices=Mbtiqishiba_choices)
    qishijiu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtiqishijiu_choices)
    bashi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashi_choices)
    bashiyi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashiyi_choices)
    bashier = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashier_choices)
    bashisan = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashisan_choices)
    bashisi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashisi_choices)
    bashiwu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashiwu_choices)
    bashiliu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashiliu_choices)
    bashiqi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashiqi_choices)
    bashiba = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashiba_choices)
    bashijiu = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtibashijiu_choices)
    jiushi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtijiushi_choices)
    jiushiyi = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtijiushiyi_choices, null=True)
    jiushier = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtijiushier_choices, null=True)
    jiushisan = models.SmallIntegerField(verbose_name="哪一个词语更合你心意", choices=Mbtijiushisan_choices, null=True)
