学习笔记
1. pandas主要分为两种数据类型：series和dataframe。series偏向一维数组，dataframe偏向二维数组。
2. dataframe会默认将第一行作为表头，通过命令添加的表头会替代第一行的数据；pd切片按行输出时表头不计入在内，输出为column_x到column_y-1行的数据
3. 导入excel、txt数据时要注意添加表头，避免漏数据；导入导出excel需要依赖xlrd/xlwd模块（但是不需要import导入）
4. pandas直接过滤数据输出的是Bool类型的true/false，如要输出实际值需要外面再加上载入的pandas变量。
通过dropna删除的空值为正行数据删除，生产慎用
5. matplotlib展示多字段的时候可以选择
plot(index,字段1,字段2,字段3...)将多个曲线放在同一个图中
也可以使用plt.figure(1)创建一个名称为figure 1的图表
subplot(numRows, numCols, plotNum)创建x行y列的第n个子图表,注：行是从下往上计算
ax1 = plt.subplot(2,1,2)
ax2 = plt.subplot(2,2,1)
ax3 = plt.subplot(2,2,2)
然后针对每个subplot进行绘图
plt.sca(ax1)
plt.plot(df.index,df['A'])
plt.sca(ax2)
plt.plot(df.index,df['B'])
plt.sca(ax3)
plt.plot(df.index,df['C'],df['D'])