# docs

## 页面优先级

- [ ] 首页demo
- [ ] 内部资料
- [ ] 科研成果/项目博客 并行
- [ ] 实验成员介绍


## 前后端接口对接

### 文件资源

#### 表
对应表：resource
```
_id:            <mongodb_id>
update_time:    '2018-12-27 09:00:00'
name:           'Generative Image Inpainting'
class:          'paper'/'share'
format:         'pdf'/'ppt'/'doc'
file:           文件句柄
```

#### API

##### GET api/resource
```
GET http://localhost/api/resource?class=paper
```
##### POST api/resource
```
POST http://localhost/api/resource
{
    name:
    class:
    format:
    file:
}
```
#### DELETE api/resource
```
DELETE http://localhost/api/resource
{
    name: 'Generative Image Inpainting'
}
```