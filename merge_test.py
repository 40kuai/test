def sayhi(name):
    print("Hello {name}!".format(name=name))
    print("start test")
###   merge 使用方法
  - git branch -b dev   创建新的分支
    - git checkout dev    手动切换到dev分支
      - git merge dev       在master上合并dev分支
        - 提交
	        git add .
		        git commit -m "merge test"
			        git push origin master
