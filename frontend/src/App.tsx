import { Paper } from "@mui/material";
import { useEffect, useState } from "react";
import MenuPrincipal from "./components/MenuPrincipal";
import MenuPlatillo from "./components/MenuPlatillo";
import MenuDinero from "./components/MenuDinero";
import MenuComensales from "./components/MenuComensales";
import MenuResultados from "./components/MenuResultados";
import axios from "axios";
import { Results } from "./models";

export interface Comensales {
  hombresMayores: number;
  hombresMenores: number;
  mujeresMayores: number;
  mujeresMenores: number;
}

function App() {
  const [menu, setMenu] = useState(1);
  const [platilloSeleccionado, setPlatilloSeleccionado] = useState("");
  const [dinero, setDinero] = useState(2000);
  const [comensales, setComensales] = useState<Comensales>({
    hombresMayores: 0,
    hombresMenores: 0,
    mujeresMayores: 0,
    mujeresMenores: 0,
  });
  const [results, setResults] = useState<Results>({
    cantidad_carne: 0,
    cortes: [
      {
        nombre: "",
        precio_corte: 0,
        precio_total: 0,
      },
    ],
  });


  const cambiarMenu = (opcion: number) => {
    setMenu(opcion);
  };
  const selectPlatillo = (platillo: string) => {
    setPlatilloSeleccionado(platillo);
    setMenu(3);
  };

  const onChangeComensales = (comensales:Comensales) => {
      setComensales(comensales)
      getResults(comensales)

  }
  const getResults = async (c:Comensales) => {
    const API_URL = "http://0.0.0.0:8000/results";
    console.log("comensales")
    console.log(c)
    const userInput = {
      platillo_a_preparar: platilloSeleccionado,
      cantidad_de_dinero: dinero,
      comensales: {
          "cantidad_hombres_mayores":c.hombresMayores,
          "cantidad_hombres_menores":c.hombresMenores,
          "cantidad_mujeres_mayores":c.mujeresMayores,
          "cantidad_mujeres_menores":c.mujeresMenores,
      },
    };
    console.log(userInput);
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userInput),
    });
    // axios.defaults.baseURL = API_URL
    // const response = await axios.post("/results",userInput);
    // const client = axios.create({})
    const result = await response.json();
    console.log(result)

    setResults({
      cantidad_carne: result["cantidad_carne"],
      cortes: result["cortes"],
    });
    cambiarMenu(5);
  };
  return (
    <Paper
      elevation={12}
      sx={{
        position: "absolute",
        width: "55%",
        height: "75%",
        // backgroundColor: "#E5E7EB",
        left: "50%",
        top: "50%",
        p: 10,
        transform: "translate(-50%, -50%)",
        borderRadius: 4,
      }}
    >
      {menu === 1 && <MenuPrincipal cambiarMenu={cambiarMenu} />}
      {menu === 2 && (
        <MenuPlatillo
          cambiarMenu={cambiarMenu}
          selectPlatillo={selectPlatillo}
        />
      )}
      {menu === 3 && (
        <MenuDinero
          dinero={dinero}
          changeDinero={(dinero) => {
            setDinero(dinero);
          }}
          cambiarMenu={cambiarMenu}
        />
      )}
      {menu === 4 && (
        <MenuComensales
          comensales={comensales}
          changeComensales={onChangeComensales
          }
          getResults={getResults}
          cambiarMenu={cambiarMenu}
        />
      )}
      {menu === 5 && (
        <MenuResultados cambiarMenu={cambiarMenu} results={results} />
      )}
    </Paper>
  );
}

export default App;
