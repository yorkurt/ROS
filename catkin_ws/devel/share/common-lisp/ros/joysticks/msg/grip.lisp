; Auto-generated. Do not edit!


(cl:in-package joysticks-msg)


;//! \htmlinclude grip.msg.html

(cl:defclass <grip> (roslisp-msg-protocol:ros-message)
  ((grip
    :reader grip
    :initarg :grip
    :type cl:fixnum
    :initform 0)
   (roll
    :reader roll
    :initarg :roll
    :type cl:fixnum
    :initform 0)
   (pan
    :reader pan
    :initarg :pan
    :type cl:fixnum
    :initform 0))
)

(cl:defclass grip (<grip>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <grip>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'grip)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name joysticks-msg:<grip> is deprecated: use joysticks-msg:grip instead.")))

(cl:ensure-generic-function 'grip-val :lambda-list '(m))
(cl:defmethod grip-val ((m <grip>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:grip-val is deprecated.  Use joysticks-msg:grip instead.")
  (grip m))

(cl:ensure-generic-function 'roll-val :lambda-list '(m))
(cl:defmethod roll-val ((m <grip>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:roll-val is deprecated.  Use joysticks-msg:roll instead.")
  (roll m))

(cl:ensure-generic-function 'pan-val :lambda-list '(m))
(cl:defmethod pan-val ((m <grip>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joysticks-msg:pan-val is deprecated.  Use joysticks-msg:pan instead.")
  (pan m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <grip>) ostream)
  "Serializes a message object of type '<grip>"
  (cl:let* ((signed (cl:slot-value msg 'grip)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'roll)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'pan)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <grip>) istream)
  "Deserializes a message object of type '<grip>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'grip) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'roll) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pan) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<grip>)))
  "Returns string type for a message object of type '<grip>"
  "joysticks/grip")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'grip)))
  "Returns string type for a message object of type 'grip"
  "joysticks/grip")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<grip>)))
  "Returns md5sum for a message object of type '<grip>"
  "c0cbb4ca42bcf7d679dd2c2e5b180f1c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'grip)))
  "Returns md5sum for a message object of type 'grip"
  "c0cbb4ca42bcf7d679dd2c2e5b180f1c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<grip>)))
  "Returns full string definition for message of type '<grip>"
  (cl:format cl:nil "int16 grip~%int16 roll~%int16 pan~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'grip)))
  "Returns full string definition for message of type 'grip"
  (cl:format cl:nil "int16 grip~%int16 roll~%int16 pan~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <grip>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <grip>))
  "Converts a ROS message object to a list"
  (cl:list 'grip
    (cl:cons ':grip (grip msg))
    (cl:cons ':roll (roll msg))
    (cl:cons ':pan (pan msg))
))
