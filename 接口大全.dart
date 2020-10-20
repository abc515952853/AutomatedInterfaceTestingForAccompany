class NetworkApi {
  static final String internalVersion = "v5.0";

  static final String apiFix = "/api/$internalVersion";

  /// TODO  ———————— 上传
  /// 多文件上传
  static final String uploadMultiple = apiFix + "/Upload/Multiple";

  /// TODO  ———————— 登录
  /// 获取Token------------------------------------------------------------------------------------pass
  static final String connectToken = "/connect/token";

  /// get 获取用户信息------------------------------------------------------------------------------------none
  static final String userProfile = apiFix + "/User/Profile";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 陪伴记录
  /// get 获取陪伴预约; post -> 添加计划
  static final String schedule = apiFix + "/Schedule";

  /// get 获取陪伴(患者)的陪伴记录 id
  static String patientAccompany(int id) => apiFix + "/Patient/$id/Accompany";

  /// get 获取患者详情 id
  static String patientId(int id) => apiFix + "/Patient/$id";

  /// post 添加陪伴记录
  static final String accompany = apiFix + "/Accompany";

  /// /// get 获取陪伴记录详情
  static String accompanyId(int id) => apiFix + "/Accompany/$id";

  /// get 今日陪伴预约
  static final String scheduleUndone = apiFix + "/Schedule/Undone";

  /// 获取患者列表,可根据关键词搜索（患者姓名）
  static final String patient = apiFix + "/Patient";

  /// 陪伴获取虚拟电话
  static final String patientVirtualPhone = apiFix + "/Patient/VirtualPhone";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 我的
  /// 获取当前用户帐户余额(所有人)-----------------------------------------------------------------------------------pass
  static final String accountBalance = apiFix + "/Account/Balance";

  /// 获取当前用户帐户流水(所有人)-----------------------------------------------------------------------------------pass
  static final String accountMyLines = apiFix + "/Account/MyLines";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 提现
  /// 提现审请(所有人)-----------------------------------------------------------------------------------pass
  static final String withdraw = apiFix + "/Withdraw";

  /// 提现账号-----------------------------------------------------------------------------------pass
  static final String userAccount = apiFix + "/User/Account";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 公共
  /// post 更新友盟 token
  static final String userUmengToken = apiFix + "/User/UmengToken";

  /// post 更新极光 token-----------------------------------------------------------------------------------pass
  static final String userJPush = apiFix + "/Jiguang/Token";

  /// get 获取版本更新策略-----------------------------------------------------------------------------------pass
  static String versionCheck(String accessToken, String platform) =>
      apiFix + "/Version/$accessToken/$platform";

  /// get 检查更新-----------------------------------------------------------------------------------pass
  static String versionCheckToken(String accessToken, String platform) =>
      apiFix + "/Version/check/$accessToken/$platform";

  /// 病种类型---------------------------------------------------------------------------------pass
  static final String publicDiseaseType = apiFix + "/Public/diseaseType";

  /// 检索病种列表---------------------------------------------------------------------------------pass
  static final String publicDisease = apiFix + "/Public/disease";

  /// 根据病种类型查询病种列表 xxx/1---------------------------------------------------------------------------------pass
  static String publicDiseaseId(int diseaseTypeId) => apiFix + "/Public/disease/$diseaseTypeId";

  /// 根据类型获取商品 未使用---------------------------------------------------------------------------------none
  static final String productType = apiFix + "/Product/type";

  /// 根据商品编号获取商品 code DL000003
  static String productCode(String code) => apiFix + "/Product/$code";

  /// TODO ————————— 商品

  /// 购买桑黄商品列表
  static final String productHomeList = apiFix + "/Product/HomeList";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 用户
  /// 提交认证审核----------------------------------------------------------------------------------------pass
  static final String certification = apiFix + "/Certification";

  /// 获取用户信息----------------------------------------------------------------------------------------pass
  static final String userMy = apiFix + "/User/My";

  /// 修改头像----------------------------------------------------------------------------------------pass
  static final String userAvatar = apiFix + "/User/Avatar";

  /// post 修改昵称和区域----------------------------------------------------------------------------------------pass
  static final String userInfo = apiFix + "/User/Info";

  /// 添加收货地址Post/修改收货地址PUT----------------------------------------------------------------------------------------pass
  static final String consignee = apiFix + "/Consignee";

  /// 设置为默认地址 {地址ID}----------------------------------------------------------------------------------------pass
  static String consigneeIdDefault(String id) => apiFix + "/Consignee/$id/Default";

  /// DELETE 删除地址 {地址ID}----------------------------------------------------------------------------------------pass
  static String consigneeId(String id) => apiFix + "/Consignee/$id";

  /// 地址列表----------------------------------------------------------------------------------------pass
  static final String consigneeMy = apiFix + "/Consignee/My";

  /// 我的邀请----------------------------------------------------------------------------------------pass
  static final String invitationMy = apiFix + "/Invitation/My";

  /// 派发
  static String userIdSend(String id) => apiFix + "/User/$id/Send";

  /// 协议同意----------------------------------------------------------------------------------------------pass
  static final String protocolAgree = apiFix + "/Protocol/Agree";

  /// 查询推广员的客户列表----------------------------------------------------------------------------------------------pass
  static final String userClient = apiFix + "/User/Client";

  /// 客户拨打电话(v2.3.1)
  static String userIDCall(String id) => apiFix + "/User/$id/Call";

  /// 获取验证码------------------------------------------------------------------------------------------------------pass
  static final String smsSend = apiFix + "/SMS/Send";

  /// 邀请成为代理
  static final String userInvitation = apiFix + "/User/Invitation";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 咨询
  /// 查询可咨询次数
  static final String meEffectiveCount = apiFix + "/Me/EffectiveCount";

  /// 咨询提问请求（免费图文）
  static final String topicFreeQuestion = apiFix + "/Topic/Free/Question";

  /// 咨询提问请求（付费）
  static final String topicQuestion = apiFix + "/Topic/Question";

  /// 咨询医生服务服务配置
  static final String topicServicePrice = apiFix + "/Topic/ServicePrice";

  /// 咨询问题列表， 咨询问题详情/（拼接ID）
  static final String topic = apiFix + "/Topic";

  /// 咨询问题列表， 咨询问题详情/（拼接ID）
  static String topicId(int topicId) => apiFix + "/Topic/$topicId";

  /// 咨询回答请求
  static String topicAnswer(int topicId) => apiFix + "/Topic/$topicId/Answer";

  /// 执行小秘书（右上角关闭事件）
  static final String topicDeleteNotice = apiFix + "/Topic/DeleteNotice";

  /// 点赞----------------------------------------------------------------------------------------------------------pass
  static final String topicPraise = apiFix + "/Topic/Praise";

  /// 接受咨询邀请(医生抢单) noticeId
  static String myIdTopicAccept(String associatedId) => apiFix + "/Me/$associatedId/TopicAccept";

  /// 电话语音咨询开始 服务Id（TopicQuestionForPhoneOutPutDto.Id）
  static String topicIdStart(int id) => apiFix + "/Topic/$id/Start";

  /// 电话语音咨询结束 服务Id（TopicQuestionForPhoneOutPutDto.Id）
  static String topicIdEnd(int id) => apiFix + "/Topic/$id/End";

  /// 我发布的咨询
  static final String meQuestions = apiFix + "/Me/Questions";

  /// 我回答的咨询
  static final String meAnswers = apiFix + "/Me/Answers";

  /// 结束咨询
  static String meIdFinish(int id) => apiFix + "/Me/$id/Finish";

  /// 咨询问题详情
  static String topicDetail(int topicId) => apiFix + "/Topic/$topicId/Detail";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 医生
  /// 医院短列表--------------------------------------------------------------------------------pass
  static final String hospitalShort = apiFix + "/Hospital/short";

  /// 医生列表（所有医生）--------------------------------------------------------------------------------pass
  static final String doctorAll = apiFix + "/Doctor/doctorAll";

  /// 医生地区--------------------------------------------------------------------------------pass
  static final String doctorDoctorArea = apiFix + "/Doctor/doctorArea";

  /// 联想医生--------------------------------------------------------------------------------pass
  static final String doctorThinkDoctor = apiFix + "/Doctor/thinkDoctor";

  /// 快速就医-提交需求
  static final String demand = apiFix + "/Demand";

  /// 医生列表（签约医生）--------------------------------------------------------------------------------pass
  static final String doctorSigning = apiFix + "/Doctor/doctorSigning";

  /// 修改医生简介
  static final String userVitae = apiFix + "/User/vitae";

  /// 我提交的需求
  static final String demandMyDemand = apiFix + "/Demand/myDemand";

  /// 科室短列表---------------------------------------------------------------------------------pass
  static String departmentId(int hospitalId) => apiFix + "/Department/$hospitalId";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 活动
  /// 根据活动编码获取信息
  static String activityCodeDetail(String code) => apiFix + "/Activity/$code/detail";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 通知
  /// 通知组列表
  static final String noticeGroup = apiFix + "/NoticeGroup";

  /// 通知列表 - 执行小秘书/订单信息通/咨询动态
  static final String notice = apiFix + "/Notice";

  /// 浏览通知（单个-设置通知为已读）
  static String noticeBrowse(int noticeId) => apiFix + "/Notice/$noticeId/browse";

  /// 浏览通知（全部-设置通知为已读）
  static String noticeBrowseAll(int groupId) => apiFix + "/Notice/$groupId/browse/all";

  /// 删除通知
  static String noticeNoticeId(int noticeId) => apiFix + "/Notice/$noticeId";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 聚合接口
  /// 首页聚合接口---------------------------------------------------------------------------------------------pass
  static final String home = apiFix + "/Home";

  /// 我的帐户
  static final String accountMy = apiFix + "/Account/My";

  /// 患者的当前登录信息
  static final String memberProfile = apiFix + "/Member/Profile";

  /// get 评价页获取医生列表 post医生
  /// topicId和orderNumber互斥
  static final String doctorReview = apiFix + "/Doctor/Review";

  /// 获取个人资料
  static final String userInformation = apiFix + "/User/Information";

  /// 立即购买-购物车列表
  static final String shoppingCartBuyNow = apiFix + "/ShoppingCart/BuyNow";

  /// 分享
  static final String appShare = apiFix + "/App/Share";

  /// 个人主页信息
  static final String userId = apiFix + "/User";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 患者
  /// 会员签约
  static final String member = apiFix + "/Member";

  /// 获取患者信息-填充到快速就医
  static final String patientDetail = apiFix + "/Patient/detail";

  /// 咨询获取虚拟电话
  static final String topicVirtualPhone = apiFix + "/Topic/VirtualPhone";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 财务
  /// 查询订单
  static final String orderQuery = apiFix + "/Order/Query";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 优惠券
  /// 查询代理可派送的优惠券
  static String couponAgentCanSendCouponId(String userId) =>
      apiFix + "/Coupon/agentCanSendCoupon/$userId";

  /// 派送优惠券
  static final String couponAgentSendCoupon = apiFix + "/Coupon/agentSendCoupon";

  /// 我的优惠券
  static final String couponMyCoupons = apiFix + "/Coupon/myCoupons";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 订单
  /// 我的订单
  static final String orderMy = apiFix + "/Order/My";

  /// 订单详情
  static final String orderDetail = apiFix + "/Order/Details";

  /// 订单取消
  static final String orderCancel = apiFix + "/Order/Cancel";

  /// 待支付订单支付
  static final String orderPay = apiFix + "/Order/Pay";

  /// 订单退款
  static final String orderRefund = apiFix + "/Order/Refund";

  /// 购物车购买-支付
  static final String shoppingCartBuy = apiFix + "/ShoppingCart/Buy";

  /// 添加购物车
  static final String shoppingCart = apiFix + "/ShoppingCart";

  /// 确认收货
  static final String orderConfirm = apiFix + "/Order/Confirm";

  /// 更新购物车数量
  static final String shoppingCartQuantity = apiFix + "/ShoppingCart/Quantity";

  /// 更新购物车数量
  static final String orderPaymentTypes = apiFix + "/Order/PaymentTypes";

  /// 医院支付 自定义支付
  static final String orderCustomizePay = apiFix + "/Order/CustomizePay";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 粉丝
  /// 我的粉丝
  static final String fanMy = apiFix + "/Fan/My";

  /// 我的关注
  static final String followMy = apiFix + "/Follow/My";

  /// 推荐
  static final String followRecommend = apiFix + "/Follow/Recommend";

  /// 关注-------------------------------------------------------------------------------------------pass
  static final String follow = apiFix + "/Follow";

  /// 取消关注
  static final String followUn = apiFix + "/Follow/Un";

  /// 全部关注
  static final String followAll = apiFix + "/Follow/All";

  /// 同步通信录
  static final String contact = apiFix + "/Contact";

  /// 小红点取消
  static final String momentsRead = apiFix + "/Moments/Read";

  /// 搜索用户
  static final String userPage = apiFix + "/Search/user";

  /// 热词数据
  static final String searchHotWords = apiFix + "/Search/hotWords";

  /// 检索综合/案例
  static final String searchAll = apiFix + "/Search/all";

// ———————————————————————————————————————————————————————————————
  /// TODO  ———————— 说说（圈子）
  /// 阳光社群----------------------------------------------------------------------------------------------------------none
  static final String moments = apiFix + "/Moments";

  /// 圈子点赞----------------------------------------------------------------------------------------------------------pass
  static String momentsIdPraise(String cycleId) => apiFix + "/Moments/$cycleId/Praise";

  /// put 删除/ get 阳光社群详情
  static String momentsId(String cycleId) => apiFix + "/Moments/$cycleId";

  /// 创建说说---------------------------------------------------------------------------------------------------pass
  static final String momentsShuoshuo = apiFix + "/Moments/Shuoshuo";

  /// 查询个人草稿数量---------------------------------------------------------------------------------------none
  static final String momentsDraftsCount = apiFix + "/Moments/Drafts/Count";

  /// 创建文章---------------------------------------------------------------------------------------none
  static final String momentsArticle = apiFix + "/Moments/Article";

  /// 推荐给所有人，本月还剩下次数---------------------------------------------------------------------------------------none
  static final String momentsPushResidueCount = apiFix + "/Moments/Push/ResidueCount";

  /// 阳光社群草稿箱---------------------------------------------------------------------------------------none
  static final String momentsDrafts = apiFix + "/Moments/Drafts";

  /// 圈子评论----------------------------------------------------------------------------------------------------------pass
  static String momentsIdComment(String cycleId) => apiFix + "/Moments/$cycleId/Comment";

  /// 用户个人动态---------------------------------------------------------------------------------------------------pass
  static final String meDynamic = apiFix + "/Me/Dynamic";

  /// 用户个人动态---------------------------------------------------------------------------------------none
  static final String momentsExternalLink = apiFix + "/Moments/ExternalLink";

  /// TODO  ———————— 代理
// ————————————————————————————————————————————————————————————————
  /// 我的团队
  static final String agentTeam = apiFix + "/Agent/Team";

  /// 申请成为千济方预备三级代理
  static final String agentApply = apiFix + "/Agent/Apply";

  /// TODO  ———————— 广场
  /// 广场栏目------------------------------------------------------------------------------------------------------pass
  static final String squareColumns = apiFix + "/Square/columns";

  /// 广场具体栏目下的列表------------------------------------------------------------------------------------------------------pass
  static final String squareSearch = apiFix + "/Square/search";

  /// TODO  ———————— 中医馆TCM
  /// 名方列表------------------------------------------------------------------------------------------------------pass
  static final String prescriptionShort = apiFix + "/Prescription/short";

  /// 中医院列表------------------------------------------------------------------------------------------------------pass
  static String tcmList(String type) => apiFix + "/Hospital/$type";

  /// 中医院详情------------------------------------------------------------------------------------------------------pass
  static String tcmDetail(int hospitalId) => apiFix + "/Hospital/$hospitalId/detail";

  /// 医院患者反馈------------------------------------------------------------------------------------------------------pass
  static String tcmDetailFeedback(int hospitalId) => apiFix + "/Hospital/$hospitalId/feedback";

  /// 提交预约------------------------------------------------------------------------------------------------------pass
  static final String hospitalScheduleSubmit = apiFix + "/HospitalSchedule/submit";

  /// 我的预约列表------------------------------------------------------------------------------------------------------pass
  static final String hospitalScheduleScheduleRecord =
      apiFix + "/HospitalSchedule/my/scheduleRecord";

  /// 我的预约详情------------------------------------------------------------------------------------------------------pass
  static String hospitalScheduleMyDetail(scheduleId) =>
      apiFix + "/HospitalSchedule/my/$scheduleId/detail";

  /// 根据预约号查询状态------------------------------------------------------------------------------------------------------pass
  static String hospitalScheduleOrderDiscount(scheduleNumber, hospitalId) =>
      apiFix + "/HospitalSchedule/$scheduleNumber/$hospitalId/order/discount";

  /// 走进中医馆项目后台首页------------------------------------------------------------------------------------------------------pass
  static final String chinaDoctorAgentMy = apiFix + "/ChinaDoctorAgent/My";

  /// 走进中医馆项目后台我的团队------------------------------------------------------------------------------------------------------pass
  static final String chinaDoctorAgentMyTeam = apiFix + "/ChinaDoctorAgent/My/Team";

  /// 走进中医馆项目后台我推荐的业务员------------------------------------------------------------------------------------------------------pass
  static final String chinaDoctorAgentMySalesman = apiFix + "/ChinaDoctorAgent/My/Salesman";

  /// 中医馆管理后台-医馆详情------------------------------------------------------------------------------------------------------pass
  static final String hospitalBackgroundManageDetail = apiFix + "/Hospital/background/manage/detail";

  /// 中医馆管理后台-修改限额------------------------------------------------------------------------------------------------------pass
  static final String hospitalBackgroundDayLimit = apiFix + "/Hospital/background/day/limit";
}
