<script setup lang="ts">
import { ref } from "vue";
import { useUsuarioStore } from "@/stores/usuarioStore";
import type { Usuario } from "@/Interfaces/usuarioInterface";
import useAuthStore from "@/stores/authStore";
import { useRouter } from "vue-router";
import { Icon } from "@iconify/vue";
import Swal from "sweetalert2";

const usuarioStore = useUsuarioStore();
const router = useRouter();
const authStore = useAuthStore();

const nombre = ref("");
const apellido = ref("");
const email = ref("");
const password = ref("");
const telefono = ref("");
const direccion = ref("");
const rol = ref<"administrador" | "veterinario" | "cliente">("cliente");
const fecha_registro = ref("");
const especialidad = ref(null);

const error = ref("");
const crearUsuario = async () => {
    if (!nombre.value || !email.value || !password.value) {
        error.value = "Nombre, email y contraseña son obligatorios.";
        return;
    }

    const nuevoUsuario: Usuario = {
        id: 0,
        nombre: nombre.value,
        apellido: apellido.value,
        email: email.value,
        password: password.value,
        telefono: telefono.value,
        direccion: direccion.value,
        rol: rol.value,
        especialidad: especialidad.value,
        disponible: true,
        fecha_registro: fecha_registro.value,
        activo: true,
    };

    try {
        await usuarioStore.crearUsuario(nuevoUsuario);

        nombre.value = "";
        apellido.value = "";
        email.value = "";
        password.value = "";
        telefono.value = "";
        direccion.value = "";
        rol.value = "cliente";
        error.value = "";

        Swal.fire({
            title: "Usuario creado",
            text: "El usuario se registró correctamente.",
            icon: "success",
            confirmButtonColor: "#6366f1",
        });
        if (authStore.usuarioAutorizado.rol == "adminisatrdor") {
            router.push({ name: "listarUsuarios" });
        } else {
            router.push({ name: "home" });
        }
    } catch (err:any) {
        error.value = "Error al crear usuario.";

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
                <Icon icon="mdi:account-plus" class="icon" />
                Crear Usuario
            </h2>

            <div v-if="error" class="error-msg">
                <Icon icon="mdi:alert-circle" /> {{ error }}
            </div>

            <form @submit.prevent="crearUsuario">
                <div class="input-group">
                    <label>Nombre</label>
                    <div class="input-box">
                        <Icon icon="mdi:account" class="input-icon" />
                        <input
                            v-model="nombre"
                            type="text"
                            placeholder="Nombre del usuario"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Apellido</label>
                    <div class="input-box">
                        <Icon icon="mdi:account" class="input-icon" />
                        <input
                            v-model="apellido"
                            type="text"
                            placeholder="Apellido del usuario"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Email</label>
                    <div class="input-box">
                        <Icon icon="mdi:email" class="input-icon" />
                        <input
                            v-model="email"
                            type="email"
                            placeholder="Correo electrónico"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Contraseña</label>
                    <div class="input-box">
                        <Icon icon="mdi:lock" class="input-icon" />
                        <input
                            v-model="password"
                            type="password"
                            placeholder="Contraseña"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Teléfono</label>
                    <div class="input-box">
                        <Icon icon="mdi:phone" class="input-icon" />
                        <input
                            v-model="telefono"
                            type="text"
                            placeholder="Teléfono"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Dirección</label>
                    <div class="input-box">
                        <Icon icon="mdi:home" class="input-icon" />
                        <input
                            v-model="direccion"
                            type="text"
                            placeholder="Dirección"
                        />
                    </div>
                </div>

                <div class="input-group">
                    <label>Rol</label>
                    <div class="input-box">
                        <Icon icon="mdi:account-cog" class="input-icon" />
                        <select v-model="rol">
                            <option value="">Seleccione un rol</option>
                            <option
                                v-if="
                                    authStore.usuarioAutorizado.rol ==
                                    'administrador'
                                "
                                value="administrador"
                            >
                                Administrador
                            </option>
                            <option
                                v-if="
                                    authStore.usuarioAutorizado.rol ==
                                    'administrador'
                                "
                                value="veterinario"
                            >
                                Veterinario
                            </option>
                            <option value="cliente">Cliente</option>
                        </select>
                    </div>
                </div>

                <div v-if="rol != 'cliente'" class="input-group">
                    <label>Especialidad</label>
                    <div class="input-box">
                        <Icon icon="mdi:stethoscope" class="input-icon" />
                        <select v-model="especialidad">
                            <option value="null">
                                Seleccione una especialidad
                            </option>
                            <option value="Clínico General">
                                Clínico General
                            </option>
                            <option value="Cirujano">Cirujano</option>
                            <option value="Anestesista">Anestesista</option>
                            <option value="Dermatologo">Dermatólogo</option>
                            <option value="Oftalmologo">Oftalmologo</option>
                        </select>
                    </div>
                </div>

                <div class="input-group">
                    <label>Fecha de Registro</label>
                    <div class="input-box">
                        <Icon icon="mdi:calendar" class="input-icon" />
                        <input v-model="fecha_registro" type="date" />
                    </div>
                </div>

                <div class="input-group">
                    <label>Disponible</label>
                    <div class="input-box">
                        <input type="checkbox" checked="true" />
                    </div>
                </div>

                <button type="submit" class="btn-submit">
                    <Icon icon="mdi:account-plus" class="btn-icon" /> Crear
                    Usuario
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
    margin-bottom: 2px;
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
