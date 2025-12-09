<script setup lang="ts">
import { ref } from "vue";
import { useServicioStore } from "@/stores/servicioStore";
import type { Servicio } from "@/Interfaces/servicioInterface";
import { useRouter } from "vue-router";
import { Icon } from "@iconify/vue";
import Swal from "sweetalert2";

const router = useRouter();
const servicioStore = useServicioStore();
import useAuthStore from "@/stores/authStore";

const nombre = ref("");
const descripcion = ref("");
const precio = ref<number | null>(null);
const duracion_estimada = ref<number | null>(null);
const error = ref("");
// const authStore =useAuthStore()

const crearServicio = async () => {
    if (
        !nombre.value ||
        precio.value === null ||
        duracion_estimada.value === null
    ) {
        error.value = "Nombre, precio y duración son obligatorios.";
        return;
    }

    const nuevoServicio: Servicio = {
        id: 0,
        nombre: nombre.value,
        descripcion: descripcion.value,
        precio: precio.value,
        duracion_estimada: duracion_estimada.value,
    };

    try {
        await servicioStore.crearServicio(nuevoServicio);

        nombre.value = "";
        descripcion.value = "";
        precio.value = null;
        duracion_estimada.value = null;
        error.value = "";

        await Swal.fire({
            title: "Servicio creado",
            text: "El servicio se registró correctamente.",
            icon: "success",
            confirmButtonColor: "#6366f1",
        });

        router.push({ name: "listarServicios" });
    } catch (err:any) {
        error.value = "Error al crear el servicio.";

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
</script>

<template>
    <div class="page">
        <div class="card">
            <h2 class="title">
                <Icon icon="mdi:briefcase-plus" class="icon" /> Crear Servicio
            </h2>

            <div v-if="error" class="error-msg">
                <Icon icon="mdi:alert-circle" /> {{ error }}
            </div>

            <form @submit.prevent="crearServicio">
                <div class="input-group">
                    <label>Nombre</label>
                    <div class="input-box">
                        <input
                            v-model="nombre"
                            type="text"
                            placeholder="Nombre del servicio"
                        />
                        <Icon icon="mdi:clipboard-text" class="input-icon" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Descripción</label>
                    <div class="input-box">
                        <textarea
                            v-model="descripcion"
                            placeholder="Descripción del servicio"
                        ></textarea>
                        <Icon icon="mdi:note-text" class="input-icon" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Precio</label>
                    <div class="input-box">
                        <input
                            v-model="precio"
                            type="number"
                            step="0.01"
                            placeholder="Precio en $"
                        />
                        <Icon icon="mdi:currency-usd" class="input-icon" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Duración estimada (minutos)</label>
                    <div class="input-box">
                        <input
                            v-model="duracion_estimada"
                            type="number"
                            placeholder="Duración"
                        />
                        <Icon icon="mdi:clock-outline" class="input-icon" />
                    </div>
                </div>

                <button type="submit" class="btn-submit">
                    <Icon icon="mdi:plus-circle" class="btn-icon" /> Crear
                    Servicio
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
.input-box select,
.input-box textarea {
    width: 100%;
    padding: 12px 12px 12px 42px;
    border-radius: 10px;
    border: 1px solid #ccc;
    transition: 0.2s ease;
    background: #fafafa;
    resize: vertical;
}

.input-box input:focus,
.input-box select:focus,
.input-box textarea:focus {
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
