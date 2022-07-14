<h2><a href="https://leetcode.com/problems/is-subsequence/">392. Is Subsequence</a></h2><h3>Easy</h3><hr><div><p>Given two strings <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">s</code> and <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">t</code>, return <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">true</code><em style="color: rgb(255, 255, 255) !important;"> if </em><code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">s</code><em style="color: rgb(255, 255, 255) !important;"> is a <strong>subsequence</strong> of </em><code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">t</code><em style="color: rgb(255, 255, 255) !important;">, or </em><code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">false</code><em style="color: rgb(255, 255, 255) !important;"> otherwise</em>.</p>

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">"ace"</code> is a subsequence of <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">"<u>a</u>b<u>c</u>d<u>e</u>"</code> while <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">"aec"</code> is not).</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;"><strong>Input:</strong> s = "abc", t = "ahbgdc"
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;"><strong>Input:</strong> s = "axc", t = "ahbgdc"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">0 &lt;= s.length &lt;= 100</code></li>
	<li><code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">0 &lt;= t.length &lt;= 10<sup>4</sup></code></li>
	<li><code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">s</code> and <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">t</code> consist only of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Suppose there are lots of incoming <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">s</code>, say <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code style="background-color: rgb(30, 43, 49) !important; color: rgb(235, 240, 242) !important;">t</code> has its subsequence. In this scenario, how would you change your code?</div>