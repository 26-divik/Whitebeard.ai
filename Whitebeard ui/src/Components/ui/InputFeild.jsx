import React from "react";

const InputFeild = ({type,id,placeholder,onChange,value,isValue,className}) => {
  return (
<div className={`${className} relative`}>
        <input
          type={type}
          id={id}
          placeholder=""
          onChange={onChange}
          value={value}
          className={`w-full border ${isValue ? 'border-tertiary' : 'border-red-600'} px-5 py-4 outline-none rounded-2xl text-primary text-lg transition-all peer mt-10 `}
        />
        <label
          htmlFor={id}
          className={` px-2 text-2xl absolute left-4 top-5 ${isValue ? 'peer-focus:text-tertiary peer-placeholder-shown:text-primary/70 text-tertiary' : 'peer-focus:text-red-600 text-red-600 peer-placeholder-shown:text-red-600/70'} peer-placeholder-shown:top-14 peer-focus:top-5 peer-focus:bg-background transition-all `} 
        >
          {placeholder}
        </label>
      </div>

  );
};

export default InputFeild;
