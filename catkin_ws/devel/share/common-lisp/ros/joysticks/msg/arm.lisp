; Auto-generated. Do not edit!


(cl:in-package joysticks-msg)


;//! \htmlinclude arm.msg.html

(cl:defclass <arm> (roslisp-msg-protocol:ros-message)
  ((joint1
    :reader joint1
    :initarg :joint1
    :type cl:fixnum
    :initform 0)
   (joint2
    :reader joint2
    :initarg :joint2
    :type cl:fixnum
    :initform 0)
   (joint3
    :reader joint3
    :initarg :joint3
    :type cl:fixnum
    :initform 0))
)

(cl:defclass arm (<arm>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <arm>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'arm)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name joysticks-msg:<arm> is deprecated: use joysticks-msg:arm instead.")))

(cl:ensure-generic-function 'joint1-val :lambda-list '(m))
(cl:defmethod joint1-val ((m <arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:joint1-val is deprecated.  Use joysticks-msg:joint1 instead.")
  (joint1 m))

(cl:ensure-generic-function 'joint2-val :lambda-list '(m))
(cl:defmethod joint2-val ((m <arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:joint2-val is deprecated.  Use joysticks-msg:joint2 instead.")
  (joint2 m))

(cl:ensure-generic-function 'joint3-val :lambda-list '(m))
(cl:defmethod joint3-val ((m <arm>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:joint3-val is deprecated.  Use joysticks-msg:joint3 instead.")
  (joint3 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <arm>) ostream)
  "Serializes a message object of type '<arm>"
  (cl:let* ((signed (cl:slot-value msg 'joint1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'joint2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'joint3)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <arm>) istream)
  "Deserializes a message object of type '<arm>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'joint1) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'joint2) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'joint3) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<arm>)))
  "Returns string type for a message object of type '<arm>"
  "joysticks/arm")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'arm)))
  "Returns string type for a message object of type 'arm"
  "joysticks/arm")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<arm>)))
  "Returns md5sum for a message object of type '<arm>"
  "eb9863fcda7de6b24e4aac39823626c2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'arm)))
  "Returns md5sum for a message object of type 'arm"
  "eb9863fcda7de6b24e4aac39823626c2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<arm>)))
  "Returns full string definition for message of type '<arm>"
  (cl:format cl:nil "int16 joint1~%int16 joint2~%int16 joint3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'arm)))
  "Returns full string definition for message of type 'arm"
  (cl:format cl:nil "int16 joint1~%int16 joint2~%int16 joint3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <arm>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <arm>))
  "Converts a ROS message object to a list"
  (cl:list 'arm
    (cl:cons ':joint1 (joint1 msg))
    (cl:cons ':joint2 (joint2 msg))
    (cl:cons ':joint3 (joint3 msg))
))
