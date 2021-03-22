# kingdee_webapi

#### 介绍
python操作金蝶云webapi，未提炼版本，原生代码处理接口逻辑

#### 软件架构
使用python3.6 + requests库 + json库 实现与金蝶云星空webapi接口对接

#### 使用说明

<p style="color:red">必须清楚的几个问题</p>

```
接口地址：金蝶的接口地址相对有点特殊，例:所有的审核为一个接口，提交为一个接口、保存为一个接口、批量保存为一个接口，他们都是唯一的，适用于所有的业务场景，比如物料的审核接口url，与采购订单的审核url一致，唯一区别在于FormId的不同

FormId的含义，业务对象表单Id，例：假设物料作为一个表单对象，则会有一个专门对应物料的FormId产生【BD_MATERIAL】，根据金蝶接口参数说明可知，所有与物料的操作相关都需传入FormId

在金蝶云BOS后台新增的自定义字段均可在webapi查到对应字段名
```



<p style="color:red">金蝶云星空字段名问题</p>

```
文本字段取值：直接字段名即可
基础资料类取值：一般为字段名+点FNAME(字段值)，字段名+点FNUMBER(编码)
辅助资料类取值：字段名+点FDataValue得到字段值，字段名+点FNUMBER得到编码
外键表取值：例采购订单明细行分录ID，取值方式为FPOOrderEntry_FEntryID，表名_主键ID字段名
```



