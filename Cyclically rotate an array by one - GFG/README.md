# Cyclically rotate an array by one
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given an array,&nbsp;rotate the&nbsp;array by one position in clock-wise direction.</span><br>
&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px; position: relative;"><span style="font-size:18px"><strong>Input:</strong>
N = 5
A[] = {1, 2, 3, 4, 5}
<strong>Output:</strong>
5 1 2 3 4</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:15px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background: rgb(15, 37, 51); padding: 5px; border-radius: 0px 0px 5px 5px; display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1&amp;title=Cyclically%20rotate%20an%20array%20by%20one%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%205%0AA%5B%5D%20%3D%20%7B1%2C%202%2C%203%2C%204%2C%205%7D%0AOutput%3A%0A5%201%202%203%204" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px; position: relative;"><span style="font-size:18px"><strong>Input:</strong>
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}
<strong>Output:</strong>
3 9 8 7 6 4 2 1</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:15px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background: rgb(15, 37, 51); padding: 5px; border-radius: 0px 0px 5px 5px; display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1&amp;title=Cyclically%20rotate%20an%20array%20by%20one%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%208%0AA%5B%5D%20%3D%20%7B9%2C%208%2C%207%2C%206%2C%204%2C%202%2C%201%2C%203%7D%0AOutput%3A%0A3%209%208%207%206%204%202%201" class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:&nbsp;&nbsp;</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>rotate()</strong>&nbsp;which takes the array <strong>A[]</strong> and its size <strong>N </strong>as inputs and modify the array in place.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong> O(N)<br>
<strong>Expected Auxiliary Space:</strong> O(1)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1&lt;=N&lt;=10<sup>5</sup><br>
0&lt;=a[i]&lt;=10<sup>5</sup></span></p>
</div>