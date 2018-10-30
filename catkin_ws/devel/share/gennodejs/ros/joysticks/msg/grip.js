// Auto-generated. Do not edit!

// (in-package joysticks.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class grip {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grip = null;
      this.roll = null;
      this.pan = null;
    }
    else {
      if (initObj.hasOwnProperty('grip')) {
        this.grip = initObj.grip
      }
      else {
        this.grip = 0;
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0;
      }
      if (initObj.hasOwnProperty('pan')) {
        this.pan = initObj.pan
      }
      else {
        this.pan = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type grip
    // Serialize message field [grip]
    bufferOffset = _serializer.int16(obj.grip, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.int16(obj.roll, buffer, bufferOffset);
    // Serialize message field [pan]
    bufferOffset = _serializer.int16(obj.pan, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type grip
    let len;
    let data = new grip(null);
    // Deserialize message field [grip]
    data.grip = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [pan]
    data.pan = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 6;
  }

  static datatype() {
    // Returns string type for a message object
    return 'joysticks/grip';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c0cbb4ca42bcf7d679dd2c2e5b180f1c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 grip
    int16 roll
    int16 pan
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new grip(null);
    if (msg.grip !== undefined) {
      resolved.grip = msg.grip;
    }
    else {
      resolved.grip = 0
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0
    }

    if (msg.pan !== undefined) {
      resolved.pan = msg.pan;
    }
    else {
      resolved.pan = 0
    }

    return resolved;
    }
};

module.exports = grip;
