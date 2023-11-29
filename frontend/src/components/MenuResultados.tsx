import { Box, Button, Grid, Typography } from "@mui/material";
import { Results } from "../models";

interface IMenuResultados {
  cambiarMenu: (opcion: number) => void;
  results: Results;
  platillo: string
}
const MenuResultados: React.FC<IMenuResultados> = ({
  cambiarMenu,
  results,
  platillo
}) => {
  return (
    <Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Box
          sx={{
            py: 2,
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <Typography
            component="h2"
            variant="h4"
            sx={{ mt: 0, color: "gray", fontWeight: "bold" }}
          >
            ¡Aqui está tu recomendación!
          </Typography>
        </Box>
      </Box>
      <Box
        sx={{
          py: 2,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography
          component="h2"
          variant="h5"
          sx={{ mt: 0, color: "gray", fontWeight: "bold" }}
        >
          Te recomendamos {results.cantidad_carne}g de estos cortes de carne
        </Typography>
        <Typography
          component="h2"
          variant="h5"
          sx={{ mt: 0, color: "gray", fontWeight: "bold" }}
        >
        para cocinar {platillo} 
        </Typography>
      </Box>
      <Box sx={{ display: "flex", justifyContent: "center" }}>
        <Grid
          container
          rowSpacing={5}
          columnSpacing={5}
          rowGap={1}
          width={"90%"}
        >
          {results.cortes.map((corte) => (
            <Grid key={corte.nombre} item xs={4}>
              <Box sx={{ backgroundColor: "#FF3C53" }}>
                <Typography
                  sx={{
                    textAlign: "center",
                    color: "white",
                    fontWeight: "bold",
                  }}
                  variant="h5"
                  component="h3"
                >
                  {corte.nombre}
                </Typography>
                <Typography
                  sx={{
                    textAlign: "center",
                    color: "white",
                    fontWeight: "bold",
                  }}
                  variant="h6"
                  component="h3"
                >
                  ${corte.precio_total}
                </Typography>
              </Box>
            </Grid>
          ))}
        </Grid>
      </Box>
      <Box
        sx={{
          mt:15,
          py: 2,
          px:9,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography
          component="h2"
          variant="h5"
          sx={{ mt: 0, color: "gray", fontWeight: "bold",textAlign:"center" }}
        >
        {results["justificacion"]}
        </Typography>
      </Box>
      <Box
        sx={{

          width: "100%",
          height:"100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "end",
          alignItems: "center",
          mt: 8,
        }}
      >
        <Button
          onClick={() => cambiarMenu(1)}
          sx={{
            width: "50%",
            backgroundColor: "#FF3C53",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            borderRadius: 20,
            ":hover": { backgroundColor: "#FF3F43" },
          }}
        >
          <Typography
            component="h4"
            variant="h4"
            sx={{ py: 2, color: "white", fontWeight: "bold" }}
          >
            Volver 
          </Typography>
        </Button>
      </Box>
    </Box>
  );
};
export default MenuResultados;
