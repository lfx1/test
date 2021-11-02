import gitlab

url='http://192.168.1.10'
token='QnXNu3EtXjKXjrszVqm9'#gitlab上的api
gl=gitlab.Gitlab(url,token)#gitlab登录
projects = gl.projects.list()#获取第一页的project
projects=gl.projects.list(all=True)#获取所有的project
projects1 = gl.projects.list(search='test')#查看项目
print(projects1)
for p in gl.projects.list(all=True,as_list=False):#获取第一页project的name,id
    print(p.name,p.id)
term=gl.projects.create({'name':'project2'})#创建一个项目
projects2=gl.projects.get(3)#通过id获取project对象
projects3=gl.projects.list(visibilty='public')#获取公开的项目
# project对象一下操作的基础
#通过指定project对象该获取项目的所有分支
branches=projects1.branches.list()#通过指定project对象获取该项目的所有分支
print(branches)
branch=projects1.branches.get('master')#获取指定分支的属性
print(branch)
branch1=term.branches.create({'branch':'feature2','ref':'master'})#创建分支
branch=projects2.branches.delete('feature2')#删除分支
# 获取指定项目的所有tags
tags=projects1.tags.list( )
#获取某个指定tag的信息
tags=projects1.tags.list('1.0')
# 创建一个tag
tag=projects1.tags.create({'tag_name':'1.0','ref':'master'})
#设置一个tag说明
tag.set_release_description('awesome v1.0 release')
# 删除tags
projects1.tags.delete('1:0')
# or
tag.delete()
# 获取所有的commit info
commits = projects1.commits.list()
for c in commits:
    print(c.author_name, c.message, c.title)
# 获取指定commit的info
commit = projects1.commits.get('e3d5a71b')
# 获取指定项目的所有merge request
mrs = projects1.mergerequests.list()
print(mrs)
# 获取 指定mr info
mr = projects1.mergerequests.get(mr_id)
#  创建一个merge request
mr = projects1.mergerequests.create({'source_branch':'cool_feature',
                                   'target_branch':'master',
                                   'title':'merge cool feature', })
# 创建一个commit
data = {
    'branch_name': 'master',  # v3
    'commit_message': 'blah blah blah',
    'actions': [
        {
            'action': 'create',
            'file_path': 'blah',
            'content': 'blah'
        }
    ]
}
commit = projects1.commits.create(data)
