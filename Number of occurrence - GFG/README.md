# Number of occurrence
## Easy
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a sorted array <strong>Arr&nbsp;</strong>of size <strong>N </strong>and a number <strong>X</strong>, you need to find the number of occurrences of<strong> X</strong> in <strong>Arr</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre style="margin-bottom: 0px; position: relative;"><span style="font-size:18px"><strong>Input:
</strong>N = 7, X = 2
Arr[] = {1, 1, 2, 2, 2, 2, 3}
<strong>Output:</strong> 4
<strong>Explanation:</strong> 2 occurs 4 times in the
given array.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:15px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background: rgb(15, 37, 51); padding: 5px; border-radius: 0px 0px 5px 5px; display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1&amp;title=Number%20of%20occurrence%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%207%2C%20X%20%3D%202%0AArr%5B%5D%20%3D%20%7B1%2C%201%2C%202%2C%202%2C%202%2C%202%2C%203%7D%0AOutput%3A%204%0AExplanation%3A%202%20occurs%204%20times%20in%20the%0Agiven%20array." class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre style="margin-bottom: 0px; position: relative;"><span style="font-size:18px"><strong>Input:
</strong>N = 7, X = 4
Arr[] = {1, 1, 2, 2, 2, 2, 3}
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;4 is not present in the
given array.</span><div class="open_grepper_editor" title="Edit &amp; Save To Grepper"></div></pre><div class="saveCodeBtnTag" style="text-align:right; margin-bottom:15px;"><span class="saveCodeBtnSpan saveCodeBtnTag" style="background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;" onmouseover="this.style=`background:#797979;;padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`" ;="" onmouseout="this.style=`background:#0f2533; padding: 5px; border-radius: 0 0 5px 5px;  display: inline-block;`;"><a src="?&amp;url=https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1&amp;title=Number%20of%20occurrence%20%7C%20Practice%20%7C%20GeeksforGeeks&amp;hashtags=&amp;code=Input%3A%0AN%20%3D%207%2C%20X%20%3D%204%0AArr%5B%5D%20%3D%20%7B1%2C%201%2C%202%2C%202%2C%202%2C%202%2C%203%7D%0AOutput%3A%200%0AExplanation%3A%C2%A04%20is%20not%20present%20in%20the%0Agiven%20array." class="saveCodeBtn saveCodeBtnTag" style="color: white; text-decoration: none; text-shadow: none; background-color: transparent;"><img src="chrome-extension://annlhfjgbkfmbbejkbdpgbmpbcjnehbb/images/saveicon.png" style="margin:0; display: inline-block; vertical-align: middle; height: 19px; width: 19px;background: #ffffff00; border: none;" class="saveCodeBtnTag"> Save</a><a></a></span></div>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>count()</strong>&nbsp;which takes the&nbsp;array of&nbsp;integers&nbsp;<strong>arr,</strong>&nbsp;<strong>n&nbsp;</strong>and<strong>&nbsp;x</strong><strong>&nbsp;</strong>as parameters and returns an integer denoting the answer.</span></p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;O(logN)<br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 ≤ N ≤ 10<sup>5</sup><br>
1 ≤ Arr[i] ≤ 10<sup>6</sup><br>
1 ≤ X ≤ 10<sup>6</sup></span></p>

<p>&nbsp;</p>
</div>