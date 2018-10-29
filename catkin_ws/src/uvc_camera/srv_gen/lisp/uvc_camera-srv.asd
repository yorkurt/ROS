
(cl:in-package :asdf)

(defsystem "uvc_camera-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "MovePTZ" :depends-on ("_package_MovePTZ"))
    (:file "_package_MovePTZ" :depends-on ("_package"))
  ))