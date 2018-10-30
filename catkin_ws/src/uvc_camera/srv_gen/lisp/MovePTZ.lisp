; Auto-generated. Do not edit!


(cl:in-package uvc_camera-srv)


;//! \htmlinclude MovePTZ-request.msg.html

(cl:defclass <MovePTZ-request> (roslisp-msg-protocol:ros-message)
  ((pan
    :reader pan
    :initarg :pan
    :type cl:fixnum
    :initform 0)
   (tilt
    :reader tilt
    :initarg :tilt
    :type cl:fixnum
    :initform 0)
   (zoom
    :reader zoom
    :initarg :zoom
    :type cl:fixnum
    :initform 0))
)

(cl:defclass MovePTZ-request (<MovePTZ-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MovePTZ-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MovePTZ-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name uvc_camera-srv:<MovePTZ-request> is deprecated: use uvc_camera-srv:MovePTZ-request instead.")))

(cl:ensure-generic-function 'pan-val :lambda-list '(m))
(cl:defmethod pan-val ((m <MovePTZ-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader uvc_camera-srv:pan-val is deprecated.  Use uvc_camera-srv:pan instead.")
  (pan m))

(cl:ensure-generic-function 'tilt-val :lambda-list '(m))
(cl:defmethod tilt-val ((m <MovePTZ-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader uvc_camera-srv:tilt-val is deprecated.  Use uvc_camera-srv:tilt instead.")
  (tilt m))

(cl:ensure-generic-function 'zoom-val :lambda-list '(m))
(cl:defmethod zoom-val ((m <MovePTZ-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader uvc_camera-srv:zoom-val is deprecated.  Use uvc_camera-srv:zoom instead.")
  (zoom m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MovePTZ-request>) ostream)
  "Serializes a message object of type '<MovePTZ-request>"
  (cl:let* ((signed (cl:slot-value msg 'pan)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'tilt)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'zoom)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MovePTZ-request>) istream)
  "Deserializes a message object of type '<MovePTZ-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pan) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'tilt) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'zoom) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MovePTZ-request>)))
  "Returns string type for a service object of type '<MovePTZ-request>"
  "uvc_camera/MovePTZRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MovePTZ-request)))
  "Returns string type for a service object of type 'MovePTZ-request"
  "uvc_camera/MovePTZRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MovePTZ-request>)))
  "Returns md5sum for a message object of type '<MovePTZ-request>"
  "a964e82c0e0401a25741502592b56334")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MovePTZ-request)))
  "Returns md5sum for a message object of type 'MovePTZ-request"
  "a964e82c0e0401a25741502592b56334")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MovePTZ-request>)))
  "Returns full string definition for message of type '<MovePTZ-request>"
  (cl:format cl:nil "~%~%int16 pan~%int16 tilt~%int16 zoom~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MovePTZ-request)))
  "Returns full string definition for message of type 'MovePTZ-request"
  (cl:format cl:nil "~%~%int16 pan~%int16 tilt~%int16 zoom~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MovePTZ-request>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MovePTZ-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MovePTZ-request
    (cl:cons ':pan (pan msg))
    (cl:cons ':tilt (tilt msg))
    (cl:cons ':zoom (zoom msg))
))
;//! \htmlinclude MovePTZ-response.msg.html

(cl:defclass <MovePTZ-response> (roslisp-msg-protocol:ros-message)
  ((rpan
    :reader rpan
    :initarg :rpan
    :type cl:fixnum
    :initform 0)
   (rtilt
    :reader rtilt
    :initarg :rtilt
    :type cl:fixnum
    :initform 0)
   (rzoom
    :reader rzoom
    :initarg :rzoom
    :type cl:fixnum
    :initform 0))
)

(cl:defclass MovePTZ-response (<MovePTZ-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MovePTZ-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MovePTZ-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name uvc_camera-srv:<MovePTZ-response> is deprecated: use uvc_camera-srv:MovePTZ-response instead.")))

(cl:ensure-generic-function 'rpan-val :lambda-list '(m))
(cl:defmethod rpan-val ((m <MovePTZ-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader uvc_camera-srv:rpan-val is deprecated.  Use uvc_camera-srv:rpan instead.")
  (rpan m))

(cl:ensure-generic-function 'rtilt-val :lambda-list '(m))
(cl:defmethod rtilt-val ((m <MovePTZ-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader uvc_camera-srv:rtilt-val is deprecated.  Use uvc_camera-srv:rtilt instead.")
  (rtilt m))

(cl:ensure-generic-function 'rzoom-val :lambda-list '(m))
(cl:defmethod rzoom-val ((m <MovePTZ-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader uvc_camera-srv:rzoom-val is deprecated.  Use uvc_camera-srv:rzoom instead.")
  (rzoom m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MovePTZ-response>) ostream)
  "Serializes a message object of type '<MovePTZ-response>"
  (cl:let* ((signed (cl:slot-value msg 'rpan)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rtilt)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rzoom)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MovePTZ-response>) istream)
  "Deserializes a message object of type '<MovePTZ-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rpan) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rtilt) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rzoom) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MovePTZ-response>)))
  "Returns string type for a service object of type '<MovePTZ-response>"
  "uvc_camera/MovePTZResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MovePTZ-response)))
  "Returns string type for a service object of type 'MovePTZ-response"
  "uvc_camera/MovePTZResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MovePTZ-response>)))
  "Returns md5sum for a message object of type '<MovePTZ-response>"
  "a964e82c0e0401a25741502592b56334")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MovePTZ-response)))
  "Returns md5sum for a message object of type 'MovePTZ-response"
  "a964e82c0e0401a25741502592b56334")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MovePTZ-response>)))
  "Returns full string definition for message of type '<MovePTZ-response>"
  (cl:format cl:nil "int16 rpan~%int16 rtilt~%int16 rzoom~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MovePTZ-response)))
  "Returns full string definition for message of type 'MovePTZ-response"
  (cl:format cl:nil "int16 rpan~%int16 rtilt~%int16 rzoom~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MovePTZ-response>))
  (cl:+ 0
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MovePTZ-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MovePTZ-response
    (cl:cons ':rpan (rpan msg))
    (cl:cons ':rtilt (rtilt msg))
    (cl:cons ':rzoom (rzoom msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MovePTZ)))
  'MovePTZ-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MovePTZ)))
  'MovePTZ-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MovePTZ)))
  "Returns string type for a service object of type '<MovePTZ>"
  "uvc_camera/MovePTZ")