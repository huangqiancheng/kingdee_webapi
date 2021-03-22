import requests

#登录url
login_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"

#单据查询url，查询集
query_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.ExecuteBillQuery.common.kdsvc"

#单个保存接口
save_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Save.common.kdsvc"

# 批量保存
save_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.BatchSave.common.kdsvc"
# 批量保存时特定参数"BatchCount"此参数为服务端开启的线程数，整型， 注（数据包数应大于此值，否则无效）例：100张订单，"BatchCount":10  意思为10张单为一批次，分10批，同时并发保存，提示效率

#提交url
submit_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Submit.common.kdsvc"

#审核url
audit_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Audit.common.kdsvc"

#下推url
push_url = "http://IP地址/K3Cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.Push.common.kdsvc"

#登录需要的Data数据包
#acctid：数据库ID标识，可在webapi中查看
#username：用户名，使用administrator即可
#password：用户密码
#lcid：默认2052
login_data = {"acctid": "", "username": "", "password": "", "lcid": ""}


# 登录方法，保存cookies
def login():
    login_response = requests.post(url=login_url, data=login_data)
    return login_response.cookies



