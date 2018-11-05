
(cl:in-package :asdf)

(defsystem "joysticks-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "arm" :depends-on ("_package_arm"))
    (:file "_package_arm" :depends-on ("_package"))
    (:file "arm" :depends-on ("_package_arm"))
    (:file "_package_arm" :depends-on ("_package"))
    (:file "drive" :depends-on ("_package_drive"))
    (:file "_package_drive" :depends-on ("_package"))
    (:file "drive" :depends-on ("_package_drive"))
    (:file "_package_drive" :depends-on ("_package"))
    (:file "grip" :depends-on ("_package_grip"))
    (:file "_package_grip" :depends-on ("_package"))
    (:file "grip" :depends-on ("_package_grip"))
    (:file "_package_grip" :depends-on ("_package"))
  ))