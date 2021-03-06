from fractions import Fraction
class Solution(object):
    # 统计在直线上点的个数
    def num_points_on_line(self, k, b, points):
        num = 0
        for i in range(len(points)):
            if points[i][0] * k + b == points[i][1]:
                num += 1
        return num

    def time_out(self, points):
        """
        暴力搜索的方法，目前自己能想到的方法
        找到两个点求出斜率，然后确定还有多少个点在上面，找到最大的, 暴力搜索不出意外的Time out了，下面尝试对代码进行优化
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        max_num = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                if points[i][0] - points[j][0] == 0: # 为纵轴的情况
                    cur_num = 0
                    for m in range(len(points)):
                        if points[m][0] == points[i][0]:
                            cur_num += 1
                else:
                    k = Fraction((points[i][1] - points[j][1]) , (points[i][0] - points[j][0]))
                    b = points[i][1] - k * points[i][0]
                    cur_num = self.num_points_on_line(k, b, points)
                if cur_num > max_num:
                    max_num = cur_num
        return max_num

    def maxPoints(self, points):
        """
        不出意料的暴力搜索的代码直接裂开了，下面看了一下别人的思路
        可以使用如下方法：
            固定一个点来统计和其他的点的斜率
            最后再将斜率和b相同的点个数统计，返回最大的值
            考虑用字典来记录，字典：{斜率: [位于当前斜率上的点]}
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        max_num = 0
        k_num = dict()
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                if points[i][0] - points[j][0] == 0: # 为纵轴的情况  斜率不存在用对应的x值的字符串表示
                    if str(points[i][0]) not in k_num.keys():
                        k_num[str(points[i][0])] = []
                    if points[i] not in k_num[str(points[i][0])]:
                        k_num[str(points[i][0])].append(points[i])
                    if points[j] not in k_num[str(points[i][0])]:
                        k_num[str(points[i][0])].append(points[j])
                    if len(k_num[str(points[i][0])]) > max_num:
                        max_num = len(k_num[str(points[i][0])])
                else:
                    k = Fraction((points[i][1] - points[j][1]) , (points[i][0] - points[j][0]))
                    b = points[i][1] - k * points[i][0]
                    key = str(k)+','+str(b)
                    if key not in k_num.keys():
                        k_num[key] = []
                    if points[i] not in k_num[key]:
                        k_num[key].append(points[i])
                    if points[j] not in k_num[key]:
                        k_num[key].append(points[j])
                    if len(k_num[key]) > max_num:
                        max_num = len(k_num[key])
        return max_num
if __name__ == '__main__':
    s = Solution()
    print(s.maxPoints([[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]))
