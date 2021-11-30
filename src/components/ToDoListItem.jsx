import React from "react";

const ToDoListItem = ({ item, isSelected, onCheckboxChange }) => (
<div>
  <label>
    <input 
      type="checkbox"
      name={item.assignmentID}
      checked={isSelected}
      onChange={onCheckboxChange}
      className="form-check-input"
    />
    {item.assignmentName} |
    Due: {item.dueDate}
  </label>
</div>
);

export default ToDoListItem;