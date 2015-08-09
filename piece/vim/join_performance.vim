let s:lines = []
for s:n in range(10)
  call add(s:lines, "    * 注意:拡張子が`.md`の場合は`markdown`ではなく`modula2`として認識されてしまいます。その場合は以下の設定を.vimrcに記述してください")
endfor

let s:bm = benchmark#new("concat string")

function! s:bm.operator_for()
  let result = ""
  let delim  = ""
  for line in s:lines
    let result = result . delim . line
    let delim  = "\\n"
  endfor
endfunction

function! s:bm.operator_while()
  let result = ""
  let delim  = ""
  let n = 0
  let length = len(s:lines)
  while n < length
    let result = result . delim . s:lines[n]
    let delim  = "\\n"
    let n += 1
  endwhile
endfunction

function! s:bm.join()
  let tmp = []
  for line in s:lines
    call add(tmp, line)
  endfor
  let result = join(tmp, "\\n")
endfunction

call s:bm.run(3)
