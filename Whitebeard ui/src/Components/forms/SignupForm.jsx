import React from "react";
import { useState } from "react";
import InputFeild from "../ui/InputFeild";
import logo from "../../assets/logo.svg";
import Button from "../ui/Button";
import wb from "../../assets/wb.png";
import { Link,useNavigate } from "react-router-dom";
const Signup = () => {
  const navigate = useNavigate();
  const [Value, setValue] = useState({
    "First Name": "",
    "Last Name": "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [isValue, setisValue] = useState({
    "First Name": true,
    "Last Name": true,
    email: true,
    password: true,
    confirmPassword: true,
  });
  const handleChange = (e) => {
    setValue({
      ...Value,
      [e.target.id]: e.target.value,
    });
    if (e.target.value.length > 0) {
      setisValue({
        ...isValue,
        [e.target.id]: true,
      });
    } else {
      if (e.target.id === "Last Name") {
        setisValue({
          ...isValue,
          [e.target.id]: true,
        });
        return;
      } else {
        setisValue({
          ...isValue,
          [e.target.id]: false,
        });
      }
    }
  };
  return (
    <div className="w-1/2 h-full flex flex-col bg-background gap-5 items-center justify-center px-10 py-10  ">
      <div className="text-center w-full">
        <h1 className="text-primary lg:text-xl text-xs">
          JOIN THE CREW BY FILLING OUT THE FORM
        </h1>
        <h1 className="text-primary lg:text-sm text-2xs">
          ALREADY A MEMBER?{" "}
          <Link
            className="text-tertiary hover:opacity-90 transition-opacity"
            to="/login"
          >
            LOGIN
          </Link>
        </h1>
      </div>

      <div className="w-full p-5 ">
        <div className="flex w-full justify-evenly">
          <InputFeild
            className={"w-2/5"}
            type="name"
            id="First Name"
            placeholder="First Name"
            onChange={handleChange}
            value={Value["First Name"]}
            isValue={isValue["First Name"]}
          />
          <InputFeild
            className={"w-2/5"}
            type="name"
            id="Last Name"
            placeholder="Last Name"
            onChange={handleChange}
            value={Value["Last Name"]}
            isValue={isValue["Last Name"]}
          />
        </div>
        <div className="flex flex-col items-center justify-center w-full">
          <InputFeild
            type="email"
            id="email"
            className={"w-22/25"}
            placeholder="Email"
            onChange={handleChange}
            value={Value.email}
            isValue={isValue.email}
          />
          <InputFeild
            className={"w-22/25"}
            type="password"
            id="password"
            placeholder="Password"
            onChange={handleChange}
            value={Value["password"]}
            isValue={isValue["password"]}
          />
          <InputFeild
            className={"w-22/25"}
            type="password"
            id="confirmPassword"
            placeholder="Confirm Password"
            onChange={handleChange}
            value={Value["confirmPassword"]}
            isValue={isValue["confirmPassword"]}
          />
        </div>
      </div>
      <div>
        <Button onClick={() => {navigate("/login")}} text="Next" />
      </div>
    </div>
  );
};

export default Signup;
