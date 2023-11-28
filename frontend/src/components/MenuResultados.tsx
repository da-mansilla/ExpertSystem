import { Box, IconButton, Slider, Typography, styled } from "@mui/material";
import StartIcon from "@mui/icons-material/Start";
import { Results } from "../models";

interface IMenuResultados {
  cambiarMenu: (opcion: number) => void;
  results: Results 
}
const MenuResultados: React.FC<IMenuResultados> = ({cambiarMenu,results}) => {
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
        <Typography variant="h4" component="h1">
            ¡Aqui está tu recomendación!
        </Typography>
      </Box>
      <Box>
        <Typography variant="h5" component="h3">
            Cantidad recomendada {results.cantidad_carne} 
        </Typography>
        {results.cortes.map(corte => (
        <Typography variant="h5" component="h3">
            {corte.nombre} - {corte.precio_corte} - {corte.precio_total}
        </Typography>

        ))}

      </Box>
    </Box>
  );
};
export default MenuResultados
