# LeetCode-Solutions
My own solutions of leetcode

#### 1047
<img src="./figs/1047.png">

* 每次遍历找到重复字母，删除后循环，O(n^2)
* 用栈来遍历字符串，入栈元素与栈顶比较，相同出栈一个字母否则入栈一个字母，最终的栈即为答案，O^(n)