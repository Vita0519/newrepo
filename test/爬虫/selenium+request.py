import time
import requests
import json
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


# 实例化一个浏览器
chrome = webdriver.WebDriver(executable_path='Driver/chromedriver_80.exe')

# 打开一个网页，以bilibili登录页面为例
# 在浏览器中输入账号与密码，当然也可以通过代码实现查找对应输入框输入文本
chrome.get("https://passport.bilibili.com/login")

# 构造“会话”
sess = requests.Session()

sess.headers.clear()

sess.headers.setdefault('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36')


# 获取cookies
cookies = chrome.get_cookies()
# 填充cookies
for cookie in cookies:
	sess.cookies.set(cookie['name'], cookie['value'])

# 直接将浏览器开发者工具中显示的Requests Payload复制下来，然后包成一个字符串
payload = '{"payload": "{\"3064\":1,\"5062\":\"1676532347959\",\"03bf\":\"https%3A%2F%2Flive.bilibili.com%2Fblackboard%2Fdropdown-menu.html\",\"39c8\":\"888.2421.fp.risk\",\"34f1\":\"\",\"d402\":\"\",\"654a\":\"\",\"6e7c\":\"nullxnull\",\"3c43\":{\"2673\":0,\"5766\":24,\"6527\":0,\"7003\":1,\"807e\":1,\"b8ce\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41\",\"641c\":0,\"07a4\":\"zh-CN\",\"1c57\":8,\"0bd0\":16,\"748e\":[900,1440],\"d61f\":[852,1440],\"fc9d\":-480,\"6aa9\":\"Asia/Shanghai\",\"75b8\":1,\"3b21\":1,\"8a1c\":1,\"d52f\":\"not available\",\"adca\":\"Win32\",\"80c9\":[[\"Microsoft Edge PDF Plugin\",\"Portable Document Format\",[[\"application/x-google-chrome-pdf\",\"pdf\"]]],[\"Microsoft Edge PDF Viewer\",\"\",[[\"application/pdf\",\"pdf\"]]],[\"Native Client\",\"\",[[\"application/x-nacl\",\"\"],[\"application/x-pnacl\",\"\"]]]],\"13ab\":\"EAAAAABJRU5ErkJggg==\",\"bfe9\":\"kABZJRAGAlYzWJooB9Bf4HxpgVtdFzGkMAAAAASUVORK5CYII=\",\"a3c1\":[\"extensions:ANGLE_instanced_arrays;EXT_blend_minmax;EXT_color_buffer_half_float;EXT_disjoint_timer_query;EXT_float_blend;EXT_frag_depth;EXT_shader_texture_lod;EXT_texture_compression_bptc;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;EXT_sRGB;KHR_parallel_shader_compile;OES_element_index_uint;OES_fbo_render_mipmap;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_color_buffer_float;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_debug_shaders;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context;WEBGL_multi_draw\",\"webgl aliased line width range:[1, 1]\",\"webgl aliased point size range:[1, 1024]\",\"webgl alpha bits:8\",\"webgl antialiasing:yes\",\"webgl blue bits:8\",\"webgl depth bits:24\",\"webgl green bits:8\",\"webgl max anisotropy:16\",\"webgl max combined texture image units:32\",\"webgl max cube map texture size:16384\",\"webgl max fragment uniform vectors:1024\",\"webgl max render buffer size:16384\",\"webgl max texture image units:16\",\"webgl max texture size:16384\",\"webgl max varying vectors:30\",\"webgl max vertex attribs:16\",\"webgl max vertex texture image units:16\",\"webgl max vertex uniform vectors:4096\",\"webgl max viewport dims:[32767, 32767]\",\"webgl red bits:8\",\"webgl renderer:WebKit WebGL\",\"webgl shading language version:WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)\",\"webgl stencil bits:0\",\"webgl vendor:WebKit\",\"webgl version:WebGL 1.0 (OpenGL ES 2.0 Chromium)\",\"webgl unmasked vendor:Google Inc. (Intel)\",\"webgl unmasked renderer:ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)\",\"webgl vertex shader high float precision:23\",\"webgl vertex shader high float precision rangeMin:127\",\"webgl vertex shader high float precision rangeMax:127\",\"webgl vertex shader medium float precision:23\",\"webgl vertex shader medium float precision rangeMin:127\",\"webgl vertex shader medium float precision rangeMax:127\",\"webgl vertex shader low float precision:23\",\"webgl vertex shader low float precision rangeMin:127\",\"webgl vertex shader low float precision rangeMax:127\",\"webgl fragment shader high float precision:23\",\"webgl fragment shader high float precision rangeMin:127\",\"webgl fragment shader high float precision rangeMax:127\",\"webgl fragment shader medium float precision:23\",\"webgl fragment shader medium float precision rangeMin:127\",\"webgl fragment shader medium float precision rangeMax:127\",\"webgl fragment shader low float precision:23\",\"webgl fragment shader low float precision rangeMin:127\",\"webgl fragment shader low float precision rangeMax:127\",\"webgl vertex shader high int precision:0\",\"webgl vertex shader high int precision rangeMin:31\",\"webgl vertex shader high int precision rangeMax:30\",\"webgl vertex shader medium int precision:0\",\"webgl vertex shader medium int precision rangeMin:31\",\"webgl vertex shader medium int precision rangeMax:30\",\"webgl vertex shader low int precision:0\",\"webgl vertex shader low int precision rangeMin:31\",\"webgl vertex shader low int precision rangeMax:30\",\"webgl fragment shader high int precision:0\",\"webgl fragment shader high int precision rangeMin:31\",\"webgl fragment shader high int precision rangeMax:30\",\"webgl fragment shader medium int precision:0\",\"webgl fragment shader medium int precision rangeMin:31\",\"webgl fragment shader medium int precision rangeMax:30\",\"webgl fragment shader low int precision:0\",\"webgl fragment shader low int precision rangeMin:31\",\"webgl fragment shader low int precision rangeMax:30\"],\"6bc5\":\"Google Inc. (Intel)~ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)\",\"ed31\":0,\"72bd\":0,\"097b\":0,\"52cd\":[0,0,0],\"a658\":\"TypeError: Cannot read properties of undefined (reading "appendChild")\",\"d02f\":\"124.04347527516074\"},\"54ef\":\"{}\",\"8b94\":\"https%3A%2F%2Fpassport.bilibili.com%2Flogin\",\"df35\":\"51075B111-E1031-9A87-9EA2-A9389566949151347infoc\",\"07a4\":\"zh-CN\",\"5f45\":null,\"db46\":0}"}'

url = 'https://cm.bilibili.com/cm/api/fees/pc'
response = sess.post(url, data=payload).text

page_text=chrome.page_source


input = chrome.find_element(By.XPATH,"//*[@id='login-username']").send_keys("13733560730")

bottun=chrome.find_element(By.XPATH,'//*[@id="login-passwd"]').send_keys('meng19980116')

denglu=chrome.find_element(By.XPATH,'//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()

time.sleep(50000)