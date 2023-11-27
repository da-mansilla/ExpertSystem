import {
  Box,
  IconButton,
  ImageList,
  ImageListItem,
  ImageListItemBar,
  Typography,
} from "@mui/material";
import StartIcon from "@mui/icons-material/Start";

interface IMenuPlatillo {
  cambiarMenu: (opcion: number) => void;
  selectPlatillo: (platillo: string) => void;
}
const MenuPlatillo: React.FC<IMenuPlatillo> = ({
  cambiarMenu,
  selectPlatillo,
}) => {
  const platillos = [
    {
      img: "https://images.unsplash.com/photo-1551963831-b3b1ca40c98e",
      nombre: "Asado",
    },
    {
      img: "https://images.unsplash.com/photo-1551782450-a2132b4ba21d",
      nombre: "Hamburguesa",
    },
    {
      img: "https://images.unsplash.com/photo-1522770179533-24471fcdba45",
      nombre: "Choripan",
    },
    {
      img: "https://images.unsplash.com/photo-1444418776041-9c7e33cc5a9c",
      nombre: "Brochetas",
    },
    {
      img: "https://images.unsplash.com/photo-1533827432537-70133748f5c8",
      nombre: "Churrasco",
    },
    {
      img: "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62",
      nombre: "Milanesa",
    },
    {
      img: "https://images.unsplash.com/photo-1516802273409-68526ee1bdd6",
      nombre: "Lampreado",
    },
    {
      img: "https://images.unsplash.com/photo-1518756131217-31eb79b20e8f",
      nombre: "Empanadas",
    },
    {
      img: "https://images.unsplash.com/photo-1597645587822-e99fa5d45d25",
      nombre: "Albóndigas",
    },
    {
      img: "https://images.unsplash.com/photo-1567306301408-9b74779a11af",
      nombre: "Estofado",
    },
    {
      img: "https://images.unsplash.com/photo-1471357674240-e1a485acb3e1",
      nombre: "Sopa",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Guiso",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Guiso",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Locro",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Carne a la Olla",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Pastel de Papa",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Arrolado de Carne",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Pan de Carne",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Lasaña",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Canelones de Carne",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Bife",
    },
    {
      img: "https://images.unsplash.com/photo-1589118949245-7d38baf380d6",
      nombre: "Carne a la Plancha",
    },
  ];
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
          Selecciona el platillo que vas a preparar
        </Typography>
      </Box>
      <Box>
        <ImageList sx={{ height: 900 }}>
          {platillos.map((item) => (
            <ImageListItem
              key={item.img}
              sx={{ cursor: "pointer" }}
              onClick={() => selectPlatillo(item.nombre)}
            >
              <img
                srcSet={`${item.img}?w=248&fit=crop&auto=format&dpr=2 2x`}
                src={`${item.img}?w=248&fit=crop&auto=format`}
                alt={item.nombre}
                loading="lazy"
              />
              <ImageListItemBar title={item.nombre} position="below" />
            </ImageListItem>
          ))}
        </ImageList>
      </Box>
      <Box>
        <Typography component="h3" variant="h3" sx={{ mt: 20 }}>
          Comenzar
        </Typography>
        <IconButton
          onClick={() => cambiarMenu(2)}
          size="large"
          color="success"
          sx={{ width: 150, height: 150 }}
        >
          <StartIcon
            sx={{ width: 150, height: 150, p: 1, borderRadius: 20 }}
          ></StartIcon>
        </IconButton>
      </Box>
    </Box>
  );
};

export default MenuPlatillo;
