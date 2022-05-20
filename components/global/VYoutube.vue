<template>
    <div class="d-flex align-content-center justify-center">
        <youtube class="d-flex align-content-center justify-center" :video-id="id"></youtube>
    </div>
</template>

<script>
export default {
    props: {
        id: null
    }
}
</script>