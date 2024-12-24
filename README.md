# College_Py_Proj
this repo use for store college python develop class proj

### Intro
前端提交一张课堂照片和课堂代号，后端返回课堂出勤人数，缺勤人数，旁听人数和具体的缺勤与旁听学生名单。在课堂照片足够清晰的条件下，这个项目能够较好的简化课堂点名流程，为喜欢点名的老师提供某种意义上的“福音”。

### Related Packets

+ Insightface
+ Milvus
+ SQLite
+ Django
+ Vue

### Frame

+ 使用 Insightface 提取照片中的人脸并 embedding 为 512 维的向量
+ 使用 Milvus 存储人脸的特征向量
+ 在考勤时，通过在向量数据库中查询相似向量，来确定上课的学生身份
+ 从 SQLite 中调取应当上课的学生信息并进行比较
+ 返回比较结果

### Other items

+ Milvus 因为环境问题，是跑在docker上的
+ 向量数据库名称部分是硬编码

> Edit Data：24/12/14 20:11 项目尚未完成
