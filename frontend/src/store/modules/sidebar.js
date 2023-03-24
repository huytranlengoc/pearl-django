const state = {
    sidebarVisible: '',
    sidebarUnfoldable: false,
}

const getters = {

};
const actions = {

};

const mutations = {
    toggleSidebar(state) {
        state.sidebarVisible = !state.sidebarVisible
    },
    toggleUnfoldable(state) {
        state.sidebarUnfoldable = !state.sidebarUnfoldable
    },
    updateSidebarVisible(state, payload) {
        state.sidebarVisible = payload.value
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
