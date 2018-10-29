;; Auto-generated. Do not edit!


(when (boundp 'joysticks::arm)
  (if (not (find-package "JOYSTICKS"))
    (make-package "JOYSTICKS"))
  (shadow 'arm (find-package "JOYSTICKS")))
(unless (find-package "JOYSTICKS::ARM")
  (make-package "JOYSTICKS::ARM"))

(in-package "ROS")
;;//! \htmlinclude arm.msg.html


(defclass joysticks::arm
  :super ros::object
  :slots (_joint1 _joint2 _joint3 ))

(defmethod joysticks::arm
  (:init
   (&key
    ((:joint1 __joint1) 0)
    ((:joint2 __joint2) 0)
    ((:joint3 __joint3) 0)
    )
   (send-super :init)
   (setq _joint1 (round __joint1))
   (setq _joint2 (round __joint2))
   (setq _joint3 (round __joint3))
   self)
  (:joint1
   (&optional __joint1)
   (if __joint1 (setq _joint1 __joint1)) _joint1)
  (:joint2
   (&optional __joint2)
   (if __joint2 (setq _joint2 __joint2)) _joint2)
  (:joint3
   (&optional __joint3)
   (if __joint3 (setq _joint3 __joint3)) _joint3)
  (:serialization-length
   ()
   (+
    ;; int16 _joint1
    2
    ;; int16 _joint2
    2
    ;; int16 _joint3
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _joint1
       (write-word _joint1 s)
     ;; int16 _joint2
       (write-word _joint2 s)
     ;; int16 _joint3
       (write-word _joint3 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _joint1
     (setq _joint1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _joint2
     (setq _joint2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _joint3
     (setq _joint3 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get joysticks::arm :md5sum-) "eb9863fcda7de6b24e4aac39823626c2")
(setf (get joysticks::arm :datatype-) "joysticks/arm")
(setf (get joysticks::arm :definition-)
      "int16 joint1
int16 joint2
int16 joint3

")



(provide :joysticks/arm "eb9863fcda7de6b24e4aac39823626c2")


