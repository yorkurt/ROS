;; Auto-generated. Do not edit!


(when (boundp 'joysticks::grip)
  (if (not (find-package "JOYSTICKS"))
    (make-package "JOYSTICKS"))
  (shadow 'grip (find-package "JOYSTICKS")))
(unless (find-package "JOYSTICKS::GRIP")
  (make-package "JOYSTICKS::GRIP"))

(in-package "ROS")
;;//! \htmlinclude grip.msg.html


(defclass joysticks::grip
  :super ros::object
  :slots (_grip _roll _pan ))

(defmethod joysticks::grip
  (:init
   (&key
    ((:grip __grip) 0)
    ((:roll __roll) 0)
    ((:pan __pan) 0)
    )
   (send-super :init)
   (setq _grip (round __grip))
   (setq _roll (round __roll))
   (setq _pan (round __pan))
   self)
  (:grip
   (&optional __grip)
   (if __grip (setq _grip __grip)) _grip)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:pan
   (&optional __pan)
   (if __pan (setq _pan __pan)) _pan)
  (:serialization-length
   ()
   (+
    ;; int16 _grip
    2
    ;; int16 _roll
    2
    ;; int16 _pan
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _grip
       (write-word _grip s)
     ;; int16 _roll
       (write-word _roll s)
     ;; int16 _pan
       (write-word _pan s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _grip
     (setq _grip (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _roll
     (setq _roll (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _pan
     (setq _pan (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get joysticks::grip :md5sum-) "c0cbb4ca42bcf7d679dd2c2e5b180f1c")
(setf (get joysticks::grip :datatype-) "joysticks/grip")
(setf (get joysticks::grip :definition-)
      "int16 grip
int16 roll
int16 pan

")



(provide :joysticks/grip "c0cbb4ca42bcf7d679dd2c2e5b180f1c")


