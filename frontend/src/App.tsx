import { Box, Paper, Typography } from "@mui/material";
import { useState } from "react";
import MenuPrincipal from "./components/MenuPrincipal";
import MenuPlatillo from "./components/MenuPlatillo";
import MenuDinero from "./components/MenuDinero";
import MenuComensales from "./components/MenuComensales";
import MenuResultados from "./components/MenuResultados";
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
  const [_comensales, setComensales] = useState<Comensales>({
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
    justificacion: "",
  });

  const cambiarMenu = (opcion: number) => {
    setMenu(opcion);
  };
  const selectPlatillo = (platillo: string) => {
    setPlatilloSeleccionado(platillo);
    setMenu(3);
  };

  const onChangeComensales = (comensales: Comensales) => {
    setComensales(comensales);
    getResults(comensales);
  };
  const getResults = async (c: Comensales) => {
    const API_URL = "http://localhost:80/results";
    const userInput = {
      platillo_a_preparar: platilloSeleccionado,
      cantidad_de_dinero: dinero,
      comensales: {
        cantidad_hombres_mayores: c.hombresMayores,
        cantidad_hombres_menores: c.hombresMenores,
        cantidad_mujeres_mayores: c.mujeresMayores,
        cantidad_mujeres_menores: c.mujeresMenores,
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
    console.log(result);

    setResults({
      cantidad_carne: result["cantidad_carne"],
      cortes: result["cortes"],
      justificacion: result["justificacion"],
    });
    cambiarMenu(5);
  };
  return (
    <Paper
      elevation={12}
      sx={{
        position: "absolute",
        width: "65%",
        height: "85%",
        // backgroundColor: "#E5E7EB",
        left: "50%",
        top: "50%",
        transform: "translate(-50%, -50%)",
        borderRadius: 4,
        backgroundColor: "#FEE8E8",
        overflow: "auto",
      }}
    >
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          // border:1,
          py: 2,
          width: "100%",
          backgroundColor: "#FF3C53",
        }}
      >
        <Typography
          component="h1"
          variant="h4"
          sx={{ color: "white", fontWeight: "bold" }}
        >
          Sistema de Recomendacion de Carne
        </Typography>
      </Box>
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
      {menu === 4 && <MenuComensales changeComensales={onChangeComensales} />}
      {menu === 5 && (
        <MenuResultados
          cambiarMenu={cambiarMenu}
          results={results}
          platillo={platilloSeleccionado}
        />
      )}
    </Paper>
  );
}

export default App;
