langs = [
  'go',
  'csharp',
  'java',
  'js',
  'cpp',
  'ruby',
  'powershell',
  'bash',
  'php',
  'css',
  'xml',
  'python',
  'scala',
  'clojure',
  'fsharp',
  'sql'
]

file_characters_truncation_limit = 2 * 1024 # 2KB

# Qunatization according to LeCun paper (2016): "Text Understanding from Scratch"
supported_chars = "abcdefghijklmnopqrstuvwxyz0123456789-,;.!?:'/\|_@#$%^&*~`+-=<>()[]{}\" " # 70 characters including space
supported_chars_map = {} # pre-calculated vectors
pad_vector = [0 for x in supported_chars]

def _setup():
  i = 0
  for ch in supported_chars:
    vec = [0 for x in supported_chars]
    vec[i] = 1
    supported_chars_map[ch] = vec
    i += 1

_setup()

def get_lang_for_vector(one_hot_vector):
  for i in range(0, len(one_hot_vector)):
    if one_hot_vector[i]==1.0:
      return langs[i]
