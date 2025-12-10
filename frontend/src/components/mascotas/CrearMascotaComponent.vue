<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useMascotaStore } from "@/stores/mascotaStore";
import { useUsuarioStore } from "@/stores/usuarioStore";
import type { Mascota } from "@/Interfaces/mascotaInterface";
import { useRouter } from "vue-router";
import { Icon } from "@iconify/vue";
import Swal from "sweetalert2";

const usuarioStore = useUsuarioStore();
const mascotaStore = useMascotaStore();
const router = useRouter();

const nombre = ref("");
const especie = ref("");
const raza = ref("");
const edad = ref<number | null>(null);
const fecha_nacimiento = ref("");
const fecha_registro = ref("");
const sexo = ref<"Macho" | "Hembra">("Macho");
const color = ref("");
const peso = ref<number | null>(null);
const id_usuario = ref<number | null>(null);

const error = ref("");

const crearMascota = async () => {
    if (!nombre.value || !especie.value || !id_usuario.value) {
        error.value = "Nombre, especie y dueño son obligatorios.";
        return;
    }

    const nuevaMascota: Mascota = {
        id: 0,
        nombre: nombre.value,
        especie: especie.value,
        raza: raza.value,
        edad: edad.value || 0,
        fecha_nacimiento: fecha_nacimiento.value,
        fecha_registro: fecha_registro.value,
        sexo: sexo.value,
        color: color.value,
        peso: peso.value || 0,
        id_usuario: id_usuario.value,
    };

    try {
        await mascotaStore.crearMascota(nuevaMascota);

        nombre.value = "";
        especie.value = "";
        raza.value = "";
        edad.value = null;
        fecha_nacimiento.value = "";
        fecha_registro.value = "";
        sexo.value = "Macho";
        color.value = "";
        peso.value = null;
        id_usuario.value = null;
        error.value = "";

        Swal.fire({
            title: "Mascota creada",
            text: "La mascota se registró correctamente.",
            icon: "success",
            confirmButtonColor: "#6366f1",
        });

        router.push({ name: "listarMascotas" });
    } catch (err:any) {
        console.error(err);
        error.value = "Error al crear la mascota.";

        Swal.fire({
            title: "Error",
            text: `${
                err.response?.data?.msg === "Token has expired"
                    ? "Debes iniciar sesion nuevamente su token ha expirado"
                    : err.response?.data?.msg
            }`,
            icon: "error",
            confirmButtonColor: "#6366f1",
        });
    }
};

onMounted(async () => {
    await usuarioStore.obtenerUsuarios();
});
</script>

<template>
    <div class="page">
        <div class="card">
            <h2 class="title">
                <Icon icon="mdi:dog" class="icon" /> Crear Mascota
            </h2>

            <div v-if="error" class="error-msg">
                <Icon icon="mdi:alert-circle" /> {{ error }}
            </div>

            <form @submit.prevent="crearMascota">
                <div class="input-group">
                    <label>Nombre</label>
                    <div class="input-box">
                        <input
                            v-model="nombre"
                            type="text"
                            placeholder="Nombre de la mascota"
                        />
                        <Icon icon="mdi:dog-side" class="input-icon" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Especie</label>
                    <div class="input-box">
                        <input
                            v-model="especie"
                            type="text"
                            placeholder="Especie"
                        />
                        <Icon icon="mdi:paw" class="input-icon" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Raza</label>
                    <div class="input-box">
                        <input v-model="raza" type="text" placeholder="Raza" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Fecha de Nacimiento</label>
                    <div class="input-box">
                        <input v-model="fecha_nacimiento" type="date" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Fecha de Registro</label>
                    <div class="input-box">
                        <input v-model="fecha_registro" type="date" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Sexo</label>
                    <div class="input-box">
                        <select v-model="sexo">
                            <option value="Macho">Macho</option>
                            <option value="Hembra">Hembra</option>
                        </select>
                    </div>
                </div>

                <div class="input-group">
                    <label>Color</label>
                    <div class="input-box">
                        <input
                            v-model="color"
                            type="text"
                            placeholder="Color"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Peso</label>
                    <div class="input-box">
                        <input
                            v-model="peso"
                            type="number"
                            step="0.1"
                            placeholder="Peso (kg)"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Propietario</label>
                    <div class="input-box">
                        <select v-model="id_usuario">
                            <option
                                v-for="duenio in usuarioStore.usuarios.filter(
                                    (user) => user.rol === 'cliente'
                                )"
                                :key="duenio.id"
                                :value="duenio.id"
                            >
                                {{ duenio.nombre + " " + duenio.apellido }}
                            </option>
                        </select>
                        <Icon icon="mdi:account" class="input-icon" />
                    </div>
                </div>

                <button type="submit" class="btn-submit">
                    <Icon icon="mdi:plus-circle" class="btn-icon" /> Crear
                    Mascota
                </button>
            </form>
        </div>
    </div>
</template>

<style scoped>
.page {
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    padding: 20px;
    background-image: url("/img/fondo.png") !important;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

.card {
    width: 100%;
    max-width: 600px;
    background: white;
    padding: 35px;
    border-radius: 18px;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.12);
}

.title {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    margin-bottom: 20px;
}

.icon {
    font-size: 28px;
}

.error-msg {
    background: #ffdddd;
    color: #b30000;
    border-left: 4px solid #b30000;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.input-group {
    margin-bottom: 15px;
}

.input-group label {
    font-weight: 600;
    margin-bottom: 5px;
    display: block;
    margin-right: 10px;
}

.input-box {
    position: relative;
}

.input-box input,
.input-box select {
    width: 100%;
    padding: 12px 12px 12px 42px;
    border-radius: 10px;
    border: 1px solid #ccc;
    transition: 0.2s ease;
    background: #fafafa;
}

.input-box input:focus,
.input-box select:focus {
    border-color: #6366f1;
    background: white;
    outline: none;
}

.input-icon {
    position: absolute;
    top: 50%;
    left: 12px;
    transform: translateY(-50%);
    font-size: 20px;
    opacity: 0.7;
}

.btn-submit {
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 8px;
    align-items: center;
    background: #6366f1;
    color: white;
    border: none;
    padding: 14px;
    border-radius: 10px;
    font-size: 16px;
    margin-top: 10px;
    cursor: pointer;
    transition: 0.2s;
}

.btn-submit:hover {
    background: #4f46e5;
}

.btn-icon {
    font-size: 20px;
}
</style>
