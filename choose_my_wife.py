import random

__Item=[]
__Player=[]
Item_num=input('需要参考的项目数：')
Player_num=input("参加淘汰人数：")
print("=======================================")
Item_num=int(Item_num)
Player_num=int(Player_num)

if Item_num<1:
    print("至少需要一个参考项目")
    exit()
if Player_num<3:
    print("至少需要三个人参加淘汰赛")
    exit()
if Player_num<0 or Item_num<0:
    print("不许为复数")
    exit()

for i in range(Item_num):
    name=input("项目名称：")
    Weight=input("权重:")
    Weight=int(Weight)
    __Item.append({"Name":name,"Weight":Weight}) 
    print("*********************************************")
print("")
print("=======================================")
for i in range(Player_num):
    score=[]
    name=input("姓名：")
    for j in range(Item_num):
        sc=input("项目 ["+__Item[j]["Name"]+"] 得分：")
        sc=int(sc)
        score.append(sc)
    __Player.append({"Name":name,"Item_score":score,"Score":0})
    print("*********************************************")

for i in __Player:
    s=0
    for j in range(Item_num):
        s=s+int(i["Item_score"][j])*int(__Item[j]["Weight"])
    i["Score"] = s
# Now we got data
#Next we should sort these data
#Thanks to https://www.runoob.com/python3/python-sort-dictionaries-by-key-or-value.html
tmp=sorted(__Player,key = lambda i: i["Score"],reverse=True)
s=[]
print("=======================================")
print("")
for i in range(3):
    print("第"+str(i+1)+"名："+str(tmp[i]["Name"])+" 得分："+str(tmp[i]["Score"])+".")
    s.append(tmp[i])
    print("")
print("***************************************")
while True:
    num=int(input("删除第几名？："))
    num=num-1
    if num in [0,1,2]:
        print("删除第"+str(num+1)+"名选手。")
        del s[num]
        break;
    else:
        print("错误！请输入1～3：")
        continue;

print("=======================================")
print("入围选手是：")
print("")
for i in s:
    print(i["Name"])

num=int(random.randint(0,9))
print("=======================================")
print("电脑随即为您选择的结果是：")
print("---------------------------------------")
if num >5:
    print("\033[5;35;46m获胜者是： "+"\033[0m"+str(s[1]["Name"]))
else:
    print("Winner:"+str(s[0]["Name"]))

print("随机因子："+str(num))
print("---------------------------------------")
print("什么？你对电脑的选择结果不满意？那么你应该知道你想要什么了……")
exit()
