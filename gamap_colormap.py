# IDL/gamap's default WhGrYlRd color scheme

WhGrYlRd_RBG_string = """
255 255 255
252 254 255
249 254 255
246 253 255
244 252 255
241 252 255
238 251 255
235 250 255
232 250 255
229 249 255
226 248 255
223 248 255
221 247 255
218 246 255
215 246 255
212 245 255
209 245 255
206 244 255
203 243 255
200 243 255
198 242 255
195 241 255
192 241 255
189 240 255
186 239 255
183 239 255
180 238 255
177 237 255
175 237 255
172 236 255
169 235 255
166 235 255
163 234 255
160 233 255
157 233 255
154 232 255
152 231 255
149 231 255
146 230 255
143 229 255
140 229 255
137 228 255
134 228 255
131 227 255
129 226 255
126 226 255
123 225 255
120 224 255
117 224 255
114 223 255
111 222 255
108 222 255
106 221 255
103 220 255
100 220 255
97 219 255
94 218 255
91 218 255
88 217 255
86 216 255
83 216 255
80 215 255
77 214 255
74 214 255
73 213 255
75 214 251
78 215 247
81 215 243
84 216 239
87 217 235
90 217 231
93 218 227
96 219 223
99 219 219
101 220 215
104 221 211
107 221 207
110 222 203
113 223 199
116 223 195
119 224 191
122 225 187
125 225 183
127 226 179
130 227 175
133 227 171
136 228 167
139 229 162
142 229 158
145 230 154
148 231 150
150 231 146
153 232 142
156 233 138
159 233 134
162 234 130
165 235 126
168 235 122
171 236 118
174 237 114
176 237 110
179 238 106
182 239 102
185 239 98
188 240 94
191 241 90
194 241 86
197 242 82
200 243 78
202 243 74
205 244 70
208 245 66
211 245 62
214 246 58
217 247 54
220 247 50
223 248 46
225 249 42
228 249 38
231 250 34
234 251 30
237 251 26
240 252 22
243 253 18
246 253 14
249 254 10
251 255 6
254 255 2
255 254 0
255 250 0
255 246 0
255 242 0
255 238 0
255 234 0
255 230 0
255 226 0
255 222 0
255 218 0
255 214 0
255 210 0
255 206 0
255 202 0
255 198 0
255 194 0
255 190 0
255 186 0
255 182 0
255 178 0
255 174 0
255 170 0
255 166 0
255 161 0
255 157 0
255 153 0
255 149 0
255 145 0
255 141 0
255 137 0
255 133 0
255 129 0
255 125 0
255 121 0
255 117 0
255 113 0
255 109 0
255 105 0
255 101 0
255 97 0
255 93 0
255 89 0
255 85 0
255 81 0
255 77 0
255 73 0
255 69 0
255 65 0
255 61 0
255 57 0
255 53 0
255 49 0
255 45 0
255 41 0
255 37 0
255 33 0
255 29 0
255 25 0
255 21 0
255 17 0
255 13 0
255 9 0
255 5 0
255 1 0
254 0 0
251 0 0
248 0 0
246 0 0
243 0 0
240 0 0
238 0 0
235 0 0
232 0 0
230 0 0
227 0 0
224 0 0
222 0 0
219 0 0
216 0 0
214 0 0
211 0 0
208 0 0
206 0 0
203 0 0
200 0 0
198 0 0
195 0 0
192 0 0
189 0 0
187 0 0
184 0 0
181 0 0
179 0 0
176 0 0
173 0 0
171 0 0
168 0 0
165 0 0
163 0 0
160 0 0
157 0 0
155 0 0
152 0 0
149 0 0
147 0 0
144 0 0
141 0 0
139 0 0
136 0 0
133 0 0
131 0 0
128 0 0
125 0 0
123 0 0
120 0 0
117 0 0
114 0 0
112 0 0
109 0 0
106 0 0
104 0 0
101 0 0
98 0 0
96 0 0
93 0 0
90 0 0
88 0 0
85 0 0
"""

import numpy as np
from matplotlib.colors import ListedColormap
WhGrYlRd_scheme = np.fromstring(WhGrYlRd_RBG_string, sep='\t').reshape(-1,3)
WhGrYlRd = ListedColormap(WhGrYlRd_scheme/255.0)
