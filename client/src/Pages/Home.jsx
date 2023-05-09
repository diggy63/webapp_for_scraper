import React, { useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

import cardGets from "../API/CardGets";

export default function Home() {
  const [resultList, setResultList] = useState([]);
  const [searchQ, setSearchQ] = useState({ query: "" });
  async function handleSearch() {
    const list = await cardGets.getOne(searchQ);
    console.log(list);
  }
  function handleChange(e) {
    setSearchQ({ ...searchQ, [e.target.name]: e.target.value });
  }
  const viewList = resultList.map((item, idx) => {
    return <h1>Hello</h1>;
  });
  return (
    <>
      <h1>Spacer</h1>
      <h1>Search for a card</h1>
      <TextField
        value={searchQ.query}
        onChange={handleChange}
        name="query"
        id="outlined-basic"
        label="Outlined"
        variant="outlined"
      />
      <Button variant="contained" onClick={handleSearch}>
        Search
      </Button>
    </>
  );
}
