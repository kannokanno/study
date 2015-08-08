; Server
;
; [11]> (defparameter my-socket (socket-server 4321))
; MY-SOCKET
; [12]> (defparameter my-stream (socket-accept my-socket))
; MY-STREAM
; [13]> (read my-stream)
; "yo server"
; [14]> (print "what up" my-s
; my-socket  my-stream
; [14]> (print "what up" my-stream)
; "what up"
; [15]> (print "what up" my-stream)
; "what up"
; [16]> (close my-stream)
; T
; [17]> (socket-server-
; socket-server-close  socket-server-host   socket-server-port
; [17]> (socket-server-
; socket-server-close  socket-server-host   socket-server-port
; [17]> (socket-server-close my-socket)
; NIL
; [18]>

; Client
;
; [4]> (defparameter my-stream (socket-connect 4321 "127.0.0.1"))
; MY-STREAM
; [5]> (print "yo server" my-stream)
; "yo server"
; [6]> (read my-stream)
; "what up"
; [7]> (read my-stream)
; "what up"
; [8]> (close my-stream)
; T
