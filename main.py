#Tip: you need to check the id of your lesson
lesson_id_list=[447093]

#-------------------script--------------------


import requests,re,time

cookies=input('input the cookies of the lesson table site:\n')


headers={
        "Cookie": cookies,
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0)"
        }

is_success=False
times=1

while lesson_id_list:
    print('times: ',times)

    index=0

    while index < len(lesson_id_list):

        lesson_id=lesson_id_list[index]
        
        res=requests.post(
        
            url="http://classes.tju.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=2808",
            headers=headers,
            data={"optype":"true","operator0":f"{lesson_id}:true:0"}
        
        )
        
        res_fail=re.search(r'失败', res.text)
        res_success=re.search(r'成功', res.text)

        if not (res_fail or res_success):
        
            print(res.text)
            print('please check your cookies')
        
        elif res_fail:
            
            print('    ', lesson_id, ' : failed')
        
        elif res_success:
            
            lesson_id_list.remove(lesson_id)
            index -= 1
            
            print('    ', lesson_id, ' : succeed')
        
        index += 1
        time.sleep(0.51)

    times += 1
